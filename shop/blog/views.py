from rest_framework.response import Response
from rest_framework.views import APIView
from blog.serializers import *
from blog.models import *


class BlogView(APIView):
    def get(self, request, format=None):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
