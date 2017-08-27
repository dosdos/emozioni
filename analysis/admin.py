# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Emotion, Search


@admin.register(Emotion)
class EmotionAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}
    list_display = ('name', 'slug', 'category')
    search_fields = ('name', 'slug', 'category')
    readonly_fields = ('creation_date', 'last_change_date')


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    list_display = ('query', 'user', 'creation_date')
    search_fields = ('query', )

    def get_readonly_fields(self, request, obj=None):
        return [field.name for field in self.model._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
