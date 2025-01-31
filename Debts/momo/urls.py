from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('weblogs/', views.PostList.as_view(), name='blogs'), 
    path('about/', views.about, name='about'),
    path('progress/', views.tmln, name='progress'),
    path('story/', views.synopsis, name='story'),
    path('privacy-policy/', views.PrivacyPolicy, name='privacyPolicy'),
    path('thank-you/', views.ty, name='thank_you'),
    path('characters/', views.characters, name='characters'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
] 
