# from django.contrib.auth.models import User
from .models import MyUser
from rest_framework import viewsets
# from .serializers import UserSerializer
from djoser.views import UserViewSet
# from .serializers import MyUserSerializer

# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


'''class MyUserViewSet(UserViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer
'''