from django.contrib import admin
from .models import Project
from modeltranslation.admin import TranslationAdmin

@admin.register(Project)
class ProjectAdmin(TranslationAdmin):
    list_display = ['name']
    prepopulated_fields = {"slug": ("name",)}



