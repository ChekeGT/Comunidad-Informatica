from django.shortcuts import redirect
from django.views.generic import  ListView
from django.urls import reverse_lazy
from questions.models import  Question
# Create your views here.

class HomeTemplateView(ListView):
    template_name = 'core/index.html'
    model = Question
    paginate_by = 4

    def get_queryset(self):
        queryset = self.model.objects.filter(solved=False)
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
            return redirect(reverse_lazy('solved_questions') + '?redirected')
        else:
            return super(HomeTemplateView, self).get(self, request, *args, **kwargs)

