from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny

# Create your views here.

class UserExistsCheck(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    @csrf_exempt
    def post(self,request):
        email = request.data['email']
        users = CustomUser.objects.filter(email=email).all()
        if not users:
            return JsonResponse({'status':0,'message':'User Does Not Exist'})
        
        return JsonResponse({'status':1,'is_active':users[0].is_active,'message':'User with this email already exists!'})

