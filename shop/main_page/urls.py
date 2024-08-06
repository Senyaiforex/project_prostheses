from django.urls import path
from main_page.views import *

app_name = 'main_page'
urlpatterns = [
    path('<str:page>/<int:position>', MainPageView.as_view(), name='page'),
]
