from django.urls import path, include
from .views import UserExistsCheck, AdminPageView

urlpatterns = [
    path('',include('djoser.urls')),
    path('',include('djoser.urls.jwt')),
    path('check/',UserExistsCheck.as_view(),name='user_check'),
    path('users_list/',AdminPageView.as_view(),name='admin_page_view')
]


"""
1. Logged In = Home, Topics, Solved, Logout
2. Not Logged In = Home, Topics, ForgotPassword, SignUp, Login, Activation, 
3. Not Redundant = Topics, 

"""