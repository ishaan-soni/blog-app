from .views import PostList, PostDetail
from django.urls import path

app_name = 'blog'

urlpatterns = [
    path('', PostList.as_view(), name='blog-home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]


