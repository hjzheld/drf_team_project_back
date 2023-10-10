from django.urls import path 
from . import views

urlpatterns = [
    path('', views.TagView.as_view()),
    path('<int:pk>/', views.TagView.as_view()),
]