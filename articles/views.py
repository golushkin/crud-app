from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy

class ArtilceListView(ListView):
    model = Article
    template_name = 'home.html'
    

class ArtilceProfileListView(ListView):
    model = Article
    template_name = 'articles/profile_articles.html'
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreateView(CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title','body')
    success_url = reverse_lazy('home')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)