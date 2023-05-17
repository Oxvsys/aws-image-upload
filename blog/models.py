from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    banner_image = models.ImageField(max_length=255, upload_to='blog')
    content = models.TextField()
    is_publish = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
