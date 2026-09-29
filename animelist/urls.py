from django.urls import path
from . import views

app_name='animelist'

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('posts/', views.post_tab, name='post'),
    path('feedback/', views.feedback_form, name='feedback'),
]