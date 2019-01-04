from django.urls import path
from .views import TutorialDetailView, TutorialListView, TutorialDeleteView, TutorialUpdateView, TutorialCreateView

urlpatterns = [
    path('<int:pk>/<slug:slug>/', TutorialDetailView.as_view(), name='tutorial_detail'),
    path('list/', TutorialListView.as_view(), name='tutorial_list'),
    path('delete/<int:pk>/', TutorialDeleteView.as_view(), name='tutorial_delete' ),
    path('update/<int:pk>/', TutorialUpdateView.as_view(), name='tutorial_update'),
    path('create/', TutorialCreateView.as_view(), name='tutorial_create'),
]