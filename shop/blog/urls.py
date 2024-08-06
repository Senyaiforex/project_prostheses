from django.urls import path
from blog.views import *

app_name = 'blogs'
urlpatterns = [
        path('list-blogs/', BlogView.as_view(), name='blogs'),
]
