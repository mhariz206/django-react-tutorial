from django.shortcuts import render
from rest_framework import viewsets  # added
from .serializers import TodoSerializer  # added
from .models import Todo  # added

# Create your views here.
class TodoView(viewsets.ModelViewSet):  # added
    serializer_class = TodoSerializer  # added
    queryset = Todo.objects.all()  # added
