from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['anime', 'submitted_by', 'comment']
        labels = {
            'submitted_by': 'Your name',
        }
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 5}),
        }
