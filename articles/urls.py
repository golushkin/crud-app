from django.urls import path
from . import views


urlpatterns = [
    path('',views.ArtilceListView.as_view(),name='home'),
    path(
        'articles/<int:pk>',
        views.ArticleDetailView.as_view(),
        name='article_detail'
    ),
    path(
        'articles/profile',
        views.ArtilceProfileListView.as_view(),
        name='profile_articles'
    ),
    path(
        'articles/create',
        views.ArticleCreateView.as_view(),
        name='article_create'
        ),
    path(
        'articles/<int:pk>/delete',
        views.ArticleDeleteView.as_view(),
        name='article_delete'
    ),
    path(
        'articles/<int:pk>/update',
        views.ArticleUpdateView.as_view(),
        name='article_update'
    ),
    path(
        'comment/add',
        views.CommentCreateView.as_view(),
        name='comment_create'
    ),
]