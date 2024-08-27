from rest_framework import generics
from .models import SpecialistModel, VideoModel
from .serializers import SpecialistSerializer, VideoSerializer


class SpecialistListView(generics.ListAPIView):
    queryset = SpecialistModel.objects.all()
    serializer_class = SpecialistSerializer


class VideoListView(generics.ListAPIView):
    serializer_class = VideoSerializer
    def get_queryset(self):
        page_name = self.kwargs.get('page_name')
        return VideoModel.objects.filter(page=page_name)
