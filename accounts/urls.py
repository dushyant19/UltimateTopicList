from django.urls import path, include
from .views import UserExistsCheck

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('check/',UserExistsCheck.as_view(),name='user_check')
]