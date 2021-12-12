from django.urls import path
from .views import ToggleSolvedView, TopicsList,FeedbackCreateView,TopicNameView

urlpatterns = [
    path('list/',TopicsList.as_view(),name='topic_list'),
    path('names/',TopicNameView.as_view(),name='topic_names'),
    path('feedback/create/',FeedbackCreateView.as_view()),
    path('solved/',ToggleSolvedView.as_view()),
    
]