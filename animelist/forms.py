from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    email = forms.EmailField(
        required = False,
        widget = forms.EmailInput(
            attrs={'class':'form-control', 'placeholder': 'you@example.com'}
        )
    )
    class Meta:
        model = Feedback
        fields = ['title','content', 'submitted_by']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control', 'placeholder':'Header of the feedabck form'
            }),
            'content': forms.Textarea(attrs={
                'class':'form-control', 'rows': 10, "placeholder":'Content of the feedback form'
            }),
            'submitted_by': forms.TextInput(attrs={
                'class':'form-control', 'placeholder': 'Author of the feedback form'
            }),
        }
        labels = {
            'title':'We would be glad to hear your opinion of how we could improve our website further',
            'content':'Body of the feedback form',
        }
        help_texts = {
            'title':'Please restrain from using any offensive language. We want to maintain user engagement and debate with others in a logical and formal way.'
        },
        error_texts = {
            'title': {
                'max_length': 'This header is too long',
                'required':'PLease, enter a title'
            }
        }

