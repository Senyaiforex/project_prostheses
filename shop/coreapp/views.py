from rest_framework import generics
from .models import SpecialistModel, VideoModel
from .serializers import SpecialistSerializer, VideoSerializer


class SpecialistListView(generics.ListAPIView):
    queryset = SpecialistModel.objects.all()
    serializer_class = SpecialistSerializer


class VideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    queryset = VideoModel.objects.all()
