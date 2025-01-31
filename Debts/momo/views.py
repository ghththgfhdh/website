from django.shortcuts import render

from django.shortcuts import render
from django.views import generic
from .models import Post
from django.core.paginator import Paginator

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'
    paginate_by = 10
    
#add tags and photos later.
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def index(request):
    return render(request, 'index.html')

def blog(request):
    return render(request, 'blog.html')

def about(request):
    return render(request, 'about.html')

def tmln(request):
    return render(request, 'tmln.html')

def synopsis(request):
    return render(request, 'synopsis.html')

def PrivacyPolicy(request):
    return render(request, 'policy.html')

def ty(request):
    return render(request, 'ty.html')

def characters(request):
    return render(request, 'char.html')

