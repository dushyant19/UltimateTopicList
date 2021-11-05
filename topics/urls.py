from django.urls import path
from .views import TopicsList,FeedbackCreateView

urlpatterns = [
    path('list/',TopicsList.as_view(),name='topic_list'),
    path('feedback/create/',FeedbackCreateView.as_view()),
]