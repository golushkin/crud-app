from django.urls import path
from . import views


urlpatterns = [
    path('',views.ArtilceListView.as_view(),name='home'),
    path('articles/<int:pk>',views.ArticleDetailView.as_view(),name='article_detail'),
    path('articles/profile',views.ArtilceProfileListView.as_view(),name='profile_articles'),
    path('articles/create',views.ArticleCreateView.as_view(),name='article_create'),
]