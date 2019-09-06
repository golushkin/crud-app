from django.urls import path
from . import views


urlpatterns = [
    path('',views.ArtilceList.as_view(),name='home'),
]