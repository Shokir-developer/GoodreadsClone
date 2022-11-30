from django import forms

from book.models import BookReview


class BookReviewForms(forms.ModelForm):
    stars_given = forms.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = BookReview
        fields = ('stars_given', 'comment')
