from django.urls import path 
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenBlacklistView,
)


urlpatterns = [
    path('signup/', views.UserView.as_view(), name='user_view'),
    path('api/token/', views.CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:user_id>/', views.UserProfileView.as_view(), name="profile_view"),
    path('article/<int:user_id>/', views.UserArticleView.as_view(), name='article_detail_view'),
    path('<int:user_id>/follow/', views.FollowView.as_view(), name='follow_view'),
]