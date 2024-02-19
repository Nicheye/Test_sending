from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('client/', ClientView.as_view()),
	path('client/<int:id>', ClientView.as_view()),
	path('sender/', SenderView.as_view()),
	path('sender/<int:id>', SenderView.as_view()),
    
]
