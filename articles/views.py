from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse

class ArtilceListView(ListView):
    model = Article
    template_name = 'home.html'
    

class ArtilceProfileListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'articles/profile_articles.html'

    def get_login_url(self):
        return reverse('login')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title','body')
    success_url = reverse_lazy('home')

    def get_login_url(self):
        return reverse('login')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)