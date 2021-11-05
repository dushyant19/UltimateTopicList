from typing import List
from topics.serializers import CategorySerializer, FeedbackSerializer, TopicNameSerializer, TopicSerializer, TopicListSerializer
from django.db.models.fields import CommaSeparatedIntegerField
from django.shortcuts import render
from django.http import HttpResponse
# from .scrap import Ultimate_list
from .models import Topic,Resource,Problem,Template,Category,Feedback
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

# Create your views here.


# def fill_db(request):
#     for key in Ultimate_list:
#         category = Category.objects.create(title=key)
#         print(f"{key} created")
#         for topic in Ultimate_list[key]:
#             title = topic.title
#             resources = topic.resources
#             problems = topic.problems
#             templates = topic.templates
#             difficulty = topic.difficulty
#             t = Topic.objects.create(title = title,difficulty=difficulty,category=category)
#             print(f"Topic for {title} is created")
#             for resource in resources:
#                 Resource.objects.create(link=resource,topic=t)
#             for problem in problems:
#                 Problem.objects.create(link=problem,topic=t)
#             for template in templates:
#                 Template.objects.create(link=template,topic=t)
#             print("Resources Problems and Templates created")       

#     return HttpResponse("Success")





class Everything(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'title':["in","exact"],
    }


class TopicsList(ListAPIView):
    serializer_class = TopicListSerializer
    queryset = Topic.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_fields = {
        'difficulty':["in","exact"],
        'category__title':["in","exact"],
        'title':["in","exact"]
    }

    def get(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        #print(queryset)
        return Response(TopicListSerializer(queryset).data)
    


class TopicNameView(ListAPIView):
    serializer_class=TopicNameSerializer
    queryset = Topic.objects.all()
    filter_backends = [SearchFilter]
    search_fields=['title']
    

class FeedbackCreateView(CreateAPIView):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

