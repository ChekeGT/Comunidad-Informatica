from django.urls import path
from .views import SolvedQuestionsListView, QuestionCreateView, QuestionDetailView, QuestionDeleteView
from .views import  QuestionUpdateView, Create_Comment

urlpatterns = [
    path('solved/', SolvedQuestionsListView.as_view(), name='solved_questions'),
    path('create/', QuestionCreateView.as_view(), name='create_question' ''),
    path('<int:pk>/<slug:slug>/', QuestionDetailView.as_view(), name='question_detail'),
    path('delete/<int:pk>/', QuestionDeleteView.as_view(), name='question_delete'),
    path('update/<int:pk>/', QuestionUpdateView.as_view(), name='question_update'),
    path('create/comment/<int:pk>/', Create_Comment, name='add_comment')
]