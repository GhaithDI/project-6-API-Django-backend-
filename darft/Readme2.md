from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.views import APIView
from .serializers import BoardSerializer,TopicSerializer,PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.

class BoardList(generics.ListCreateAPIView):
    queryset=Board.objects.all()
    serializer_class=BoardSerializer
           
class BoardTopics(generics.ListCreateAPIView):
     queryset=Topic.objects.all()
     serializer_class=TopicSerializer



class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
     queryset=Board.objects.all()
     serializer_class=BoardSerializer
     lookup_field='id'
            



        
