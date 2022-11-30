from django.core.paginator import Paginator
from django.shortcuts import render

from book.models import BookReview


def landing_page(request):
    return render(request, "landing_page.html")


def home_page(request):
    book_review = BookReview.objects.all().order_by("-created_at")
    paginator = Paginator(book_review, 5)
    page_num = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'home.html', {"page_obj":page_obj})