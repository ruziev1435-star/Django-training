from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Anime, Feedback, Post
from .forms import FeedbackForm

def home_page_view(request):
    animes = Anime.objects.all()
    return render(request, 'animelist/animelist_specific_template.html', {'animes': animes})
    
def post_tab(request):
    post = Post.objects.all()
    return render(request, 'animelist/post_tab.html', {'posts': post})

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your feedback was submitted.')
            return redirect('animelist:feedback')
    else:
        form = FeedbackForm()
    return render(request, 'animelist/feebbackform_page.html', {'form': form})
# Create your views here.
