from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import SpecialistModel, VideoModel
from .serializers import SpecialistSerializer, VideoSerializer


class SpecialistListView(generics.ListAPIView):
    queryset = SpecialistModel.objects.all()
    serializer_class = SpecialistSerializer


class VideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = VideoModel.objects.all()

class VideoDetailView(APIView):
    def get(self, request, slug, format=None):
        video = get_object_or_404(VideoModel, slug=slug)
        serializer = VideoSerializer(video)
        return Response(serializer.data)