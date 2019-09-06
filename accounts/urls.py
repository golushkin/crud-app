from django.urls import path
from .views import SignUpView
from django.urls import include


urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('auth/',include('social_django.urls',namespace='social')),
]