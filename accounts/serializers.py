from djoser.serializers import UserCreateSerializer,UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        model = User
        fields = ('id')

class UserSerializer(UserSerializer):
    class Meta(UserSerializer):
        model = User
        fields = ('id','email','is_active')

