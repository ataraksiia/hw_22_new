from django.urls import path
from blog.apps import BlogConfig
from blog.views import PostListView, post_detail, PostCreateView, PostUpdateView, PostDeleteView

app_name = BlogConfig.name

urlpatterns = [
       path('', PostListView.as_view(), name='post_list'),
       path('post/<int:pk>/detail', post_detail, name='post_detail'),
       path('post/create/', PostCreateView.as_view(), name='post_create'),
       path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
       path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
]
