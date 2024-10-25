from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('specialists/', SpecialistListView.as_view(), name='specialists'),
    path('videos/all/', VideoListView.as_view(), name='list-videos'),
    path('videos/<slug:slug>/', VideoDetailView.as_view(), name='video-detail'),
    path('videos/tags/all/', VideoTagView.as_view(), name='tag-list')
]
