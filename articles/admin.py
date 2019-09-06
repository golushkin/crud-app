from django.contrib import admin
from .models import Article,Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1

class CommentAdmin(admin.ModelAdmin):
    fields = ('article','body','author','date')
    readonly_fields = ('date',)

class ArticleAdmin(admin.ModelAdmin):
    model = Article
    inlines = [
        CommentInline,
    ]
    fields = ('title','body','author','date')
    readonly_fields = ('date',)
    date_hierarchy ='date'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
