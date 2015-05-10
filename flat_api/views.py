from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import viewsets,status,generics
from rest_framework.views import APIView
from serializers import UserAllSerializer,UserLoginSerializer,UserDetailSerializer
from django.contrib.auth import login, logout
from rest_framework.authentication import BasicAuthentication
from rest_framework.response import Response
import json
from rest_framework.decorators import api_view

#class UserView(viewsets.ModelViewSet):
#	queryset = User.objects.all()
#	serializer_class = UserSerializer
#	model = User

# detail of  users
class UserAll(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserAllSerializer
    # paginate_by = 10

# detail of single user/
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

# new user
class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLoginSerializer	

# user/login post request.
# params : username, password
class UserLoginView(APIView):

 	def post(self, request, format=None):
		user = authenticate(username=request.data['username'], password=request.data['password'])
		msg = {"message": "Invalid Username/Passowrd"}
		if user is None:
			return Response(data=msg, status=status.HTTP_200_OK)
		login(request, user)
		msg["message"] = "Logged in as : " + request.data['username']
		return Response(data=msg, status=status.HTTP_200_OK)

@api_view(['GET', ])
# user/logout ka h.
def logoutView(request):
	logout(request)
	msg = {}
	msg["message"] = "Logged out!"
	return Response(data=msg, status=status.HTTP_200_OK)
