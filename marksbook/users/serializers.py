from rest_framework import serializers
# from django.contrib.auth.models import User
# from djoser.serializers import UserSerializer
from .models import MyUser

# class UserSerializer(serializers.ModelSerializer):
#     tasks = serializers.StringRelatedField(many=True, read_only=True)

#     class Meta:
#         model = User
#         fields = ('id', 'username') #, 'tasks')
#         ref_name = 'ReadOnlyUsers'


'''class MyUserSerializer(UserSerializer):
    class Meta:
        model = MyUser
        fields = ('id', 'email', 'is_admin')  # , 'tasks')
        # ref_name = 'ReadOnlyUsers'
'''