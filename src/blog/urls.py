from django.urls import path

from blog.views import articles_list_view, dynamic_lookup_view, article_create_view

app_name='blog'
urlpatterns = [
    # path('', product_detail_view),
    path('create/', article_create_view),
    path('<int:id>/', dynamic_lookup_view, name="article-details"),
    # path('<int:my_id>/delete/', product_delete_view),
    path('', articles_list_view),
]
