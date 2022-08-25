import re
from typing import Iterable, List

from django.db.models import Case, When, Count
from django.db.models.expressions import Exists, OuterRef
from django.db.models.query import QuerySet
from django.http.response import JsonResponse
from topics.serializers import CategorySerializer, FeedbackSerializer, TopicNameSerializer, TopicSerializer, TopicListSerializer
from django.db.models.fields import BooleanField, CommaSeparatedIntegerField
from django.shortcuts import render
from django.http import HttpResponse
# from .scrap import Ultimate_list
from .models import Topic, Resource, Problem, Template, Category, Feedback
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import GenericAPIView, ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .filters import SolvedFilter, UnSolvedFilter

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
        'title': ["in", "exact"],
    }


class TopicsList(GenericAPIView):
    serializer_class = TopicListSerializer
    queryset = Topic.objects.prefetch_related("resources","templates","problems").all()
    #queryset = Topic.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'difficulty': ["in", "exact"],
        'category__title': ["in", "exact"],
        'title': ["in", "exact"]
    }

    #custom serializer

    # def serialize_topic(self, item):
    #     topic = {
    #         "title" : item.title,
    #         "difficulty" : item.difficulty,
    #         "resources" : [],
    #         "problems" : [],
    #         "templates": [],
    #         "solved" : item.solved or False
    #     }

    #     for resource in item.resources.all():
    #         topic["resources"].append({
    #             "link" : resource.link,
    #         })
        
    #     for problem in item.problems.all():
    #         topic["problems"].append({
    #             "link" : problem.link,
    #         })
    #     for template in item.templates.all():
    #         topic["templates"].append({
    #             "link" : template.link,
    #         })
        
    #     return topic

    # def get(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     print(request.user)
    #     if request.user.is_authenticated:
    #         solved_topics = request.user.profile.solved_topics
    #         queryset = queryset.annotate(
    #             solved = Exists(
    #                 solved_topics.filter(pk = OuterRef('pk'))
    #             )
    #         )
        
    #     data = []
    #     for category in Category.objects.all().order_by("created_at"):
    #         iterable = queryset.filter(category__pk = category.pk)
    #         category_data = {"title" : category.title, "topics" : []}
    #         for item in iterable.all():
    #             category_data['topics'].append(self.serialize_topic(item))

    #         data.append(category_data)

      
    #     return Response(data)

    
    def get(self, request):
        if request.user.is_authenticated:
            self.filter_backends.insert(0,SolvedFilter)
        
        queryset = self.filter_queryset(self.get_queryset())

        print(request.user)
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            solved_topics = request.user.profile.solved_topics
            queryset = queryset.annotate(
                solved = Exists(
                    solved_topics.filter(pk = OuterRef('pk'))
                )
            )
        
        return Response(TopicListSerializer(queryset).data)


class TopicNameView(ListAPIView):
    serializer_class = TopicNameSerializer
    queryset = Topic.objects.all()
    filter_backends = [SearchFilter]
    search_fields = ['title']


class FeedbackCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()

class ToggleSolvedView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        topic_id = request.data['id']
        topic = Topic.objects.get(id=topic_id)
        user = request.user

        solved_topics = user.profile.solved_topics
        filter_topics = solved_topics.filter(id=topic_id)
        
        if not filter_topics:
            solved_topics.add(topic)
        else:
            solved_topics.remove(topic)
        
        user.profile.solved_topics.set(list(solved_topics.all()))
        user.profile.save()

        return JsonResponse({"Message": "Successful"})


