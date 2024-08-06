from rest_framework import generics
from .models import SpecialistModel
from .serializers import SpecialistSerializer


class SpecialistListView(generics.ListAPIView):
    queryset = SpecialistModel.objects.all()
    serializer_class = SpecialistSerializer
