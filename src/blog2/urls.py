from django.urls import path

from .views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

app_name='blog2'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view()),
    path('<int:id>/', ArticleDetailView.as_view(), name="article-details"),
    path('<int:id>/update', ArticleUpdateView.as_view()),
    path('<int:id>/delete', ArticleDeleteView.as_view()),
    # # path('<int:my_id>/delete/', product_delete_view),
    # path('', articles_list_view),
]
