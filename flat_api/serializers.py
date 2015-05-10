from django.contrib.auth.models import User
from rest_framework import serializers
import pdb
import re

# Check if email already exists.
def mail_validator(data):
    users = User.objects.filter(email=data)
    if(len(users) > 0):
        raise serializers.ValidationError("Email already exists")
# For password minimum string length 6.
# @Todo username string validation.
def pass_validator(data):
    if(len(data) < 6):
        raise serializers.ValidationError("Password Too short")

def uname_validator(data):
    matchObj = re.match( r'/^[a-zA-Z]+[a-zA-Z0-9\.\_\-]*[a-zA-Z0-9]$/', data)
    if matchObj  is not None:
        raise serializers.ValidationError("Invalid username")        
    

class UserAllSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators = [mail_validator])
    username = serializers.CharField(validators = [uname_validator],write_only=True)
    password = serializers.CharField(validators = [pass_validator],write_only=True)
    class Meta:
        model = User
        fields = ('id','username','password', 'first_name', 'email')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    # create new user
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password', 'first_name', 'email')
        write_only_fields = ('password',)

    # Update user information
    def update(self, instance, validated_data):
        instance.set_password(validated_data.get('password', instance.password))
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')
