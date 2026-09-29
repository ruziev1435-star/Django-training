from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['title', 'anime', 'submitted_by', 'email', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Header of the feedback form'
            }),
            'anime': forms.Select(attrs={'class':'form-control'}),
            'submitted_by': forms.TextInput(attrs={
                'class':'form-control', 'placeholder': 'Author of the feedback form'
            }),
            'email': forms.EmailInput(attrs={
                'class':'form-control', 'placeholder': 'you@example.com'
            }),
            'content': forms.Textarea(attrs={
                'class':'form-control', 'rows': 10, "placeholder":'Content of the feedback form'
            }),
        }
        labels = {
            'title':'We would be glad to hear your opinion of how we could improve our website further',
            'anime':'Which anime is this about? (optional)',
            'submitted_by':'Your Name',
            'email':'Email (optional)',
            'content':'Body of the feedback form',
        }
        help_texts = {
            'title':'Please refrain from using any offensive language. We want to maintain user engagement and debate with others in a logical and formal way.',
            'email':"e.g. yourname@gmail.com — only if you'd like a reply.",
        }
        error_messages = {
            'title': {
                'max_length': 'This header is too long',
                'required':'Please, enter a title'
            }
        }
