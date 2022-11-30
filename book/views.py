from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, DetailView

from book.forms import BookReviewForms
from book.models import Book, BookReview


# class BookList(ListView):
#     template_name = "books/list.html"
#     queryset = Book.objects.all()
#     context_object_name = "books"

class BookList(View):
    def get(self, request):
        books = Book.objects.all().order_by("id")

        search_query = request.GET.get('q', '')
        if search_query:
            books = books.filter(title__icontains=search_query)

        paginator = Paginator(books, 4)
        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)

        context = {"page_obj": page_obj, "q": search_query}
        return render(request, "books/list.html", context)


class BookDetailView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)

        review_form = BookReviewForms()
        context = {"book": book, 'review_form': review_form}
        return render(request, "books/detail.html", context)


class AddReviewView(View):
    def post(self, request, id):
        book = Book.objects.get(id=id)
        review_form = BookReviewForms(data=request.POST)

        if review_form.is_valid():
            BookReview.objects.create(
                book=book,
                user=request.user,
                stars_given=review_form.cleaned_data['stars_given'],
                comment=review_form.cleaned_data['comment']
            )
            return redirect(reverse("books:detail", kwargs={'id':book.id}))

        context = {"book": book, 'review_form': review_form}
        return render(request, "books/detail.html", context)


class EditReviewView(LoginRequiredMixin, View):
    def get(self, request, book_id, review_id):
        return render(request, 'books/edit_review.html')
