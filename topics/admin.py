from django.contrib import admin
from django.db.models import fields
from django.contrib import admin
from .models import *

# class TopicAdmin(admin.AdminSite):
#     fields = ("title", "id", "created_at", "difficulty", "category")
# class CategoryAdmin(admin.ModelAdmin):
#      fields = ("title","created_at")

admin.site.register(Topic)
admin.site.register(Problem)
admin.site.register(Resource)
admin.site.register(Template)
admin.site.register(Category)
admin.site.register(Feedback)


# Register your models here.
