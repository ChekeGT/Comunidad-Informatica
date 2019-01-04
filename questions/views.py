from django import  forms
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.http import Http404, JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Question, Comment

# Create your views here.
class SolvedQuestionsListView(ListView):
    template_name = 'core/index.html'
    model = Question
    paginate_by = 4

    def get_queryset(self):
        queryset = self.model.objects.filter(solved=True)
        if len(queryset) == 0 and len(self.model.objects.all()) == 0:
            return 0
        elif len(queryset) == 0 and len(self.model.objects.all()) >= 1:
            return 1
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset == 0:
            return redirect(reverse_lazy('create_question'))
        elif queryset == 1:
            return redirect(reverse_lazy('home' + '?redirected'))
        else:
            return super(SolvedQuestionsListView, self).get(self, request, *args, **kwargs)


@method_decorator(login_required(), name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    template_name = 'questions/create_or_update_question.html'
    fields = ('title', 'description', 'language')

    def get_success_url(self):
        return  reverse_lazy('question_detail', args=[self.object.pk, slugify(self.object.title)])

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(QuestionCreateView, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(QuestionCreateView, self).get_form()
        form.fields['title'].widget = forms.TextInput(attrs={'placeholder':'Titulo:', 'class':'form-control mb-3 mt-3'})
        form.fields['description'].widget = forms.Textarea(attrs={'placeholder':'Descripcion:', 'class':'form-control mb-3 mt-2'})
        form.fields['language'].widget = forms.TextInput(attrs={'placeholder':'Lenguaje:', 'class':'form-control mb-3 mt-2'})
        form.fields['language'].label = ''
        form.fields['title'].label = ''
        form.fields['description'].label = ''
        return  form


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'questions/question_detail.html'

@method_decorator(login_required(), name='dispatch')
class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'core/delete_item.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super(QuestionDeleteView, self).get_object()
        if obj.author == self.request.user:
            return obj
        else:
            raise Http404


@method_decorator(login_required(), name='dispatch')
class QuestionUpdateView(UpdateView):
    model = Question
    template_name = 'questions/create_or_update_question.html'
    fields = ('title', 'description', 'language')

    def get_success_url(self):
        return  reverse_lazy('question_detail', args=[self.object.pk, slugify(self.object.title)])

    def get_object(self, queryset=None):
        obj = super(QuestionUpdateView, self).get_object()

        if obj.author == self.request.user:
            return obj
        else:
            raise Http404

    def get_form(self, form_class=None):
        form = super(QuestionUpdateView, self).get_form()
        form.fields['title'].widget = forms.TextInput(attrs={'placeholder':'Titulo:', 'class':'form-control mb-3 mt-3'})
        form.fields['description'].widget = forms.Textarea(attrs={'placeholder':'Descripcion:', 'class':'form-control mb-3 mt-2'})
        form.fields['language'].widget = forms.TextInput(attrs={'placeholder':'Lenguaje:', 'class':'form-control mb-3 mt-2'})
        form.fields['language'].label = ''
        form.fields['title'].label = ''
        form.fields['description'].label = ''
        return  form

@login_required()
def Create_Comment(request, pk):
    json_response = {'created':False}
    question = Question.objects.get(pk=pk)
    comment = request.GET.get('comment')
    if comment:
        try:
            comment = Comment.objects.create(text=comment, author=request.user)
            question.comments.add(comment)
            if comment.author == question.author:
                    if comment.text.lower() == 'resuelto':
                        question.solved = True
                        question.save()
        except Exception as e:
            print(type(e).__name__)
        else:
            json_response['created'] = True
    return JsonResponse(json_response)