from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Post
from .forms import FeedbackForm


def home_page_view(request):
    return render(request, 'animelist/animelist_specific_template.html')

def post_tab(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'animelist/post_tab.html', {'posts': posts})

def feedback_form(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your feedback has been sent.')
            return redirect('animelist:home')
        # if invalid, fall through to the render below,
        # reusing this same `form` so its errors show up
    else:
        form = FeedbackForm()

    context = {
        'form': form,
        'page_title': 'Share your feedback with us',
    }
    return render(request, 'animelist/feedbackform_page.html', context)
