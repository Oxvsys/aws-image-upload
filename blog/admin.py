from django.contrib import admin

from blog import models


@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "is_publish", "is_featured", "created_at", "updated_at"]
    list_filter = ["is_publish", "is_featured", "created_at"]
