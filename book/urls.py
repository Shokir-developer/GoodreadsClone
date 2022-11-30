from django.urls import path

from book.views import BookList, BookDetailView, AddReviewView, EditReviewView

app_name = "books"

urlpatterns = [
    path("", BookList.as_view(), name="list"),
    path("<int:id>/", BookDetailView.as_view(), name="detail"),
    path("<int:id>/reviews/", AddReviewView.as_view(), name="reviews"),
    path("<int:book_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="edit-review"),
]