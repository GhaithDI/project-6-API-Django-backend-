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
from rest_framework import viewsets
# Create your views here.

#API FBV#:
 
#def boards_list(request):
 #          boards=Board.objects.all()
           # لهذا السبب تم استخدام ليست لانها اكثر من عنصر
  #         data={'Results':list(boards.values('pk','name','description'))}
   #        return JsonResponse(data)
#--------------------------------------------
# class BoardList(APIView):
#         def get(self,request):
#            boards=Board.objects.all()
#            data=BoardSerializer(boards,many=True).data
#            return Response(data)
        
#         def post(self,request):
#               serializer=BoardSerializer(data=request.data)
#               if serializer.is_valid():
#                     serializer.save()
#                     return Response(serializer.data,status=status.HTTP_201_CREATED)
#               return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)

# class BoardTopics(APIView):
#     def get(self, request, boards_id):
#         board = get_object_or_404(Board, pk=boards_id)
#         topics = board.topics.order_by('-created_dt').annotate(comments=Count('posts'))
#         data = TopicSerializer(topics, many=True).data
#         return Response(data)

#     def post(self, request, boards_id):
#         # نضمن أن البورد موجود
#         board = get_object_or_404(Board, pk=boards_id)

#         # إضافة ID البورد تلقائيًا للبيانات القادمة من العميل
#         data = request.data.copy()
#         data['board'] = board.id

#         serializer = TopicSerializer(data=data)
#         if serializer.is_valid():
#             topic = serializer.save()

#             # إنشاء أول بوست للموضوع
#             post_data = {
#                 'message': data.get('message'),
#                 'topic': topic.id,
#                 'created_by': topic.created_by.id,
#                 'created_dt': topic.created_dt,
#                 'updated_by': topic.updated_by.id if topic.updated_by else None,
#                 'updated_dt': topic.updated_dt,
#             }
#             post_serializer = PostSerializer(data=post_data)
#             if post_serializer.is_valid():
#                 post_serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             else:
#                 return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class BoardDetails(APIView):
#       def get(self,request,boards_id):
#             board=get_object_or_404(Board,pk=boards_id)
#             data=BoardSerializer(board).data
#             return Response(data)

#--------------------------------------#
#API GBV#:

# class BoardList(generics.ListCreateAPIView):
#     queryset=Board.objects.all()
#     serializer_class=BoardSerializer

#---------------------------------------------#           
# class BoardTopics(generics.ListCreateAPIView):
#      queryset=Topic.objects.all()
#      serializer_class=TopicSerializer
#-----------------------------------------#
# class BoardDetails(generics.RetrieveUpdateDestroyAPIView):
#      queryset=Board.objects.all()
#      serializer_class=BoardSerializer
#      lookup_field='id'

#API Viewsets#:            
class BoardViewSet(viewsets.ModelViewSet):
          queryset=Board.objects.all()
          serializer_class=BoardSerializer



        
