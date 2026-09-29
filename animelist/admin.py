from django.contrib import admin
from django.db.models import Count
from .models import Anime, Feedback

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'rating', 'feedback_count')
    list_display_links = ('title',)
    date_hierarchy = 'publication_date'
    search_fields = ('title',)

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.annotate(_feedback_count=Count('feedback'))

    @admin.display(description='Feedbacks', ordering='_feedback_count')
    def feedback_count(self, obj):
        return obj._feedback_count

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('anime', 'submitted_by', 'created_at')
    date_hierarchy = 'created_at'    
