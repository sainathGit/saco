from django.contrib import admin

# Register your models
from .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)

