from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm


# Create your views here.


def articles_list_view(request):
    queryset = Article.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, "articles/articles_list.html", context)


def dynamic_lookup_view(request, id):
    obj = get_object_or_404(Article, id=id)
    context = {"object": obj}
    return render(request, "articles/article_details.html", context)


def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, "articles/article_create.html", context)
