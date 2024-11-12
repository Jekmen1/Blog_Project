from django.urls import path
from .views import UserRegistrationView, BlogListCreateView, BlogDetailUpdateDeleteView, CommentListCreateView, CommentDetailUpdateDeleteView, CategoryListView, TagListView, MenuListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('blogs/', BlogListCreateView.as_view()),
    path('blogs/<int:pk>/', BlogDetailUpdateDeleteView.as_view()),
    path('comments/', CommentListCreateView.as_view(),
    path('comments/<int:pk>/', CommentDetailUpdateDeleteView.as_view()),
    path('categories/', CategoryListView.as_view()),
    path('tags/', TagListView.as_view()),
    path('menus/', MenuListView.as_view()))
]
