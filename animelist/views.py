from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Anime, Post
from .forms import FeedbackForm


def home_page_view(request):
    animes = Anime.objects.all()
    return render(request, 'animelist/animelist_specific_template.html', {'animes': animes})
    
def post_tab(request):
    post = Post.objects.all()
    return render(request, 'animelist/post_tab.html', {'posts': post})

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            submitted_by = form.cleaned_data['submitted_by']
            email = form.cleaned_data['email']
            print(f"The feedback is provided by {submitted_by} ({email}): {content}")
            return redirect('animelist:home')
        # if invalid, fall through to the render below,
        # reusing this same `form` so its errors show up
    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'page_title': 'Text us though Gmail to share your problems',
    }
    return render(request, 'animelist/feedbackform_page.html', context)