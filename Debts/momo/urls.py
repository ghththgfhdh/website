from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weblogs/', views.PostList.as_view(), name='blogs'), #wants blog.html
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), # wants momo/post_list
] 
