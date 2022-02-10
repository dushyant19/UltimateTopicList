from rest_framework import serializers
from .models import *
from django.db import models

class ResourceSerializer(serializers.ModelSerializer):

    class Meta:
        model= Resource
        fields = ['link']

class TemplateSerializer(serializers.ModelSerializer):

    class Meta:
        model= Template
        fields = ['link']

class ProblemSerializer(serializers.ModelSerializer):

    class Meta:
        model= Problem
        fields = ['link']


class TopicSerializer(serializers.ModelSerializer):
    resources = ResourceSerializer(many=True)
    templates = TemplateSerializer(many=True)
    problems = ProblemSerializer(many=True)
    solved = serializers.BooleanField(default=False)
    class Meta:
        model = Topic
        fields = ['id', 'title', 'difficulty', 'resources', 'templates', 'problems', 'solved']
    

class TopicListSerializer(serializers.ListSerializer):
    child = TopicSerializer()
    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        return [
            {
                'title':category.title,
                'topics':TopicSerializer(iterable.filter(category__pk=category.pk),many=True).data
            }
            for category in Category.objects.all().order_by("-rank")
        ]


class CategorySerializer(serializers.ModelSerializer):

    topics = TopicSerializer(many=True)
    class Meta:
        model= Category
        fields = ['title','topics']


class TopicNameSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Topic
        fields = ['title']


class FeedbackSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Feedback
        fields = ['title','feedback','created_at']

