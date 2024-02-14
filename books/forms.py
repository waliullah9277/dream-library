from django import forms
from .models import Review

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'rating', 'comment', 
        ]
