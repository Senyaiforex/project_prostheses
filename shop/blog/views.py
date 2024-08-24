from rest_framework.response import Response
from rest_framework.views import APIView
from blog.serializers import *
from blog.models import *
from django.shortcuts import get_object_or_404


class BlogView(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)


class BlogDetailView(APIView):
    def get(self, request, slug, format=None):
        # Найти блог по slug
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

class TagView(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)