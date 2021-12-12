from rest_framework import filters
from .models import Topic


class SolvedFilter(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        param = request.query_params.get("solved", None)

        if param == "true":
            return request.user.profile.solved_topics

        elif param == "false":
            solved_topics_ids = request.user.profile.solved_topics.values('id')

            topics = queryset.exclude(id__in=solved_topics_ids)
            return topics

        return queryset


class UnSolvedFilter(filters.BaseFilterBackend):

    def filter_queryset(self, request, queryset, view):
        topics = Topic.objects.all()
        solved_topics_ids = request.user.profile.solved_topics.values('id')

        topics = Topic.objects.exclude(id__in=solved_topics_ids)
        return topics
