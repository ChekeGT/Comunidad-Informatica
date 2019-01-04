from django.views.generic import ListView,DeleteView,DetailView,UpdateView,CreateView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django import forms
from django.http import Http404
from django.utils.text import  slugify
from django.urls import reverse_lazy
from .models import Tutorial
# Create your views here.


class TutorialDetailView(DetailView):
    model = Tutorial
    template_name = 'tutorials/tutorial_detail.html'


class TutorialListView(ListView):
    model = Tutorial
    template_name = 'tutorials/tutorial_list.html'


@method_decorator(staff_member_required(), name='dispatch')
class TutorialDeleteView(DeleteView):
    model = Tutorial
    template_name = 'core/delete_item.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super(TutorialDeleteView, self).get_object()
        if obj.author == self.request.user:
            return obj
        else:
            raise Http404


@method_decorator(staff_member_required(), name='dispatch')
class TutorialUpdateView(UpdateView):
    model = Tutorial
    template_name = 'tutorials/update_or_create_tutorial.html'
    fields = ('title', 'content','language', 'image', 'video')

    def get_success_url(self):
        return  reverse_lazy('tutorial_detail', args=[self.object.pk, slugify(self.object.title)])

    def get_object(self, queryset=None):
        obj = super(TutorialUpdateView, self).get_object()
        if obj.author == self.request.user:
            return obj
        else:
            raise Http404

    def get_form(self, form_class=None):
        form = super(TutorialUpdateView, self).get_form()
        form.fields['title'].widget = forms.TextInput(attrs={'placeholder':'Titulo:', 'class':'form-control mb-3 mt-3'})
        form.fields['content'].widget = forms.Textarea(attrs={'placeholder':'Contenido:', 'class':'form-control mb-3 mt-2'})
        form.fields['language'].widget = forms.TextInput(attrs={'placeholder':'Lenguaje:', 'class':'form-control mb-3 mt-2'})
        form.fields['language'].label = ''
        form.fields['title'].label = ''
        form.fields['content'].label = ''
        return  form


@method_decorator(staff_member_required(), name='dispatch')
class TutorialCreateView(CreateView):
    model = Tutorial
    template_name = 'tutorials/update_or_create_tutorial.html'
    fields = ('title', 'content', 'language', 'image', 'video')

    def get_success_url(self):
        return  reverse_lazy('tutorial_detail', args=[self.object.pk, slugify(self.object.title)])

    def form_valid(self, form):
        form.instance.author = self.request.user
        print(form.instance.image)
        return super(TutorialCreateView, self).form_valid(form)

    def get_form(self, form_class=None):
        form = super(TutorialCreateView, self).get_form()
        form.fields['title'].widget = forms.TextInput(
            attrs={'placeholder': 'Titulo:', 'class': 'form-control mb-3 mt-3'})
        form.fields['content'].widget = forms.Textarea(
            attrs={'placeholder': 'Contenido:', 'class': 'form-control mb-3 mt-2'})
        form.fields['language'].widget = forms.TextInput(
            attrs={'placeholder': 'Lenguaje:', 'class': 'form-control mb-3 mt-2'})
        form.fields['language'].label = ''
        form.fields['title'].label = ''
        form.fields['content'].label = ''
        return form
