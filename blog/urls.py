from django.urls import include, path
from rest_framework import routers

from blog import views


router = routers.DefaultRouter()

router.register('', views.BlogViewSet, basename='blog')

urlpatterns = [
    path('', include(router.urls), name='blogs')
]
