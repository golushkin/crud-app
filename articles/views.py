from django.views.generic import ListView
from .models import Article

class ArtilceList(ListView):
    model = Article
    template_name = 'home.html'
    success_url = 'articles:home'