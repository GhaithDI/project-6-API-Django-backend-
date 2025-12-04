from rest_framework import serializers
from .models import *
#ملاحظة مهمة :اسماء المتغيرات المتسخدمة مع فيديو نفسها لكن تم اضافة _2 الى الاسم مثل
#(board_data_2,board_serial_2)

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TopicSerializer(serializers.ModelSerializer):
    board_name = serializers.CharField(source='board.name', read_only=True)
    creator_name = serializers.CharField(source='created_by.username', read_only=True)

    class Meta:
        model = Topic
        fields = '__all__'
        # إذا أردت إرسال board عند POST
        extra_kwargs = {'board': {'write_only': True}}


class PostSerializer(serializers.ModelSerializer):
    topic_id = serializers.PrimaryKeyRelatedField(source='topic', queryset=Topic.objects.all(), write_only=True)
    topic_name = serializers.CharField(source='topic.subject', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'