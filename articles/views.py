from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Article
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

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

    def get_success_url(self):
        messages.info(self.request,'Article "{}" created'.format(self.object.title))
        success_url = reverse_lazy('home')

    def get_login_url(self):
        return reverse('login')

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'

    def get_success_url(self):
        messages.info(self.request,'Article "{}" deleted'.format(self.object.title))
        return reverse_lazy('profile_articles')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
    
    def get_login_url(self):
        return reverse('login')

class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Article
    template_name = 'articles/article_update.html'
    fields = ('title','body')
    
    def get_success_url(self):
        return reverse_lazy('profile_articles')

    def test_func(self):
        obj = self.get_object()
        return self.request.user == obj.author
    
    def get_login_url(self):
        return reverse('login')