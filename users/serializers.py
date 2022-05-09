from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import User


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'telephone_number', 'consent', 'password'
        )
        model = User
        extra_kwargs = {
            'password': {'write_only': True},
            'consent': {'write_only': True},
        }
    
    def create(self, validated_data):
        user = super(CreateUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class SelfInfoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username', 'email', 'first_name', 'last_name',
            'telephone_number', 'consent', 'delete_flag'
        )
        
        model = User


class SelfUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('delete_flag',)
        model = User


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = ('password', 'groups', 'user_permissions')
        model = User
