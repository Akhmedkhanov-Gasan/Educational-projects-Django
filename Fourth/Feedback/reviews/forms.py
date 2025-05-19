from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'
        labels = {
            'user_name': 'Your name',
            'review_text': 'Your review',
            'rating': 'Your rating',
        }
        error_messages = {
            'user_name': {
                'required': 'Your name is required Fucker!',
                'max_length': 'Your name is too long you FUCK!!',
            }
        }
