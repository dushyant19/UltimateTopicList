from django.urls import path, include
from .views import UserExistsCheck

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('check/',UserExistsCheck.as_view(),name='user_check')
]


"""
1. Logged In = Home, Topics, Solved, Logout
2. Not Logged In = Home, Topics, ForgotPassword, SignUp, Login, Activation, 
3. Not Redundant = Topics, 

"""