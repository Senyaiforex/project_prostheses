from django.urls import path
from .views import *

app_name = 'core'
urlpatterns = [
    path('specialists/', SpecialistListView.as_view(), name='specialists'),
    path('pages/<str:page_name>/videos/', VideoListView.as_view(), name='videos'),
]
