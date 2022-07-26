from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (CreateView, DetailView, ListView, UpdateView, DeleteView)

# Create your views here.


from .models import Article
from .forms import ArticleModelForm


class ArticleListView(ListView):
    template_name = 'articles/articles_list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/article_details.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    #success_url = '/'
    queryset = Article.objects.all()


class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)


class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('blog2:article-list')