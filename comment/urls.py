from django.urls import path 
from . import views

urlpatterns = [
    path('<int:article_id>/comment/', views.CommentView.as_view()),
    path('<int:article_id>/comment/<int:pk>/', views.CommentView.as_view()),
]