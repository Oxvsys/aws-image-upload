from rest_framework import viewsets

from blog import models, serializers


class BlogViewSet(viewsets.ModelViewSet):
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
    http_method_names = ["get", "post", "put", "patch", "head", "delete"]
