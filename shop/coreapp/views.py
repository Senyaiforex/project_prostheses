from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SpecialistModel, VideoModel, CategoryModel
from .serializers import SpecialistSerializer, VideoSerializer, VideoTagSerializer


class SpecialistListView(generics.ListAPIView):
    queryset = SpecialistModel.objects.filter(hidden=False)
    serializer_class = SpecialistSerializer


class VideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = VideoModel.objects.all().order_by('created_at', 'updated_at')

class VideoDetailView(APIView):
    def get(self, request, slug, format=None):
        video = get_object_or_404(VideoModel, slug=slug)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

class VideoTagView(APIView):
    def get(self, request, format=None):
        tags = CategoryModel.objects.all()
        serializer = VideoTagSerializer(tags, many=True)
        return Response(serializer.data)