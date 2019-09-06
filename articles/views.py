from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView,DeleteView,CreateView
from .models import Article, Comment
from .forms import CommentForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages

class ArtilceListView(ListView):
    model = Article
    template_name = 'home.html'
    paginate_by = 8

    def get_queryset(self):
        return Article.objects.all().order_by('-date')
    

class ArtilceProfileListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = 'articles/profile_articles.html'

    def get_login_url(self):
        return reverse('account_login')

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user).order_by('-date')
    

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/article_detail.html'

    def get_context_data(self, **kwargs): 
        context = super(ArticleDetailView, self).get_context_data(**kwargs)
        context['comment_form'] = CommentForm(
            initial= {
                'article': self.object,
                'author':self.request.user,
            }
        )
        return context

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title','body')

    def get_success_url(self):
        messages.info(self.request,'Article "{}" created'.format(self.object.title))
        return reverse('home')

    def get_login_url(self):
        return reverse('account_login')

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
        return reverse('account_login')

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
        return reverse('account_login')

class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'articles/create_comment.html'
    http_method_names = ('post',)
    form_class = CommentForm
