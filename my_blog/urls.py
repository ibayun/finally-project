from django.urls import path

from .views import *

urlpatterns = [
    path('', posts_message_test)
]