from django.urls import path
from . import views

urlpatterns = [
    path('convert/', views.text_to_audio, name='text_to_audio'),
] 