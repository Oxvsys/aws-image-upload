from rest_framework import serializers

from blog import models


class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Blog
        fields = ["id", "title", "sub_title", "banner_image", "content", "is_publish", "is_featured",
                  "created_at", "updated_at"]
