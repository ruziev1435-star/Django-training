from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime, Feedback, Post

def home_page_view(request):
    animes = Anime.objects.all()
    return render(request, 'animelist/animelist_specific_template.html', {'animes': animes})
    
def post_tab(request):
    post = Post.objects.all()
    return render(request, 'animelist/post_tab.html', {'posts': post})
# Create your views here.
