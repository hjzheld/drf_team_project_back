from django.conf import settings
from django.conf.urls.static import static
from django.urls import path 
from articles import views


urlpatterns = [
    path('', views.ArticleView.as_view(), name='articles_view'),
    path('<int:article_id>/', views.ArticleDetailView.as_view(), name='article_detail_view'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)