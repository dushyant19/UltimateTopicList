from django.conf import settings
from django.shortcuts import render
from rest_framework.views import APIView
from .models import CustomUser
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from .models import CustomUser
from rest_framework.generics import GenericAPIView,ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAdminUser
from .serializers import User, UserSerializer
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



class AdminPageView(ListAPIView):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAdminUser]
    
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_fields = {
        'is_active':["exact"]
    }
    search_fields = ['email']

    