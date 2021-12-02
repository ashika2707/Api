from django.shortcuts import render
from rest_framework import viewsets
from .serializer import LoginSerializer
from .models import Login

class LoginViewset(viewsets.ModelViewSet):
    queryset = Login.objects.all().order_by('uname')
    serializer_class = LoginSerializer
# Create your views here.
