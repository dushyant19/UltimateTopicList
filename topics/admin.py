from django.contrib import admin
from .models import *

admin.site.register(Topic)
admin.site.register(Problem)
admin.site.register(Resource)
admin.site.register(Template)
admin.site.register(Category)

# Register your models here.
