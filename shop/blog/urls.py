from django.urls import path
from blog.views import *

app_name = 'blogs'
urlpatterns = [
    path('list-blogs/', BlogView.as_view(), name='blogs'),
    path('tags/all/', TagView.as_view(), name='tags'),
    path('<slug:slug>/', BlogDetailView.as_view(), name='blog-detail'),
]