from django.test import TestCase
from django.urls import reverse

from book.models import Book


class BookTestCase(TestCase):
    def test_no_book(self):
        response = self.client.get(reverse("books:list"))
        self.assertContains(response, "No found book.")

    def test_book_list(self):
        book1 = Book.objects.create(title="Book1", description="good", isbn="1111")
        book2 = Book.objects.create(title="Book2", description="good", isbn="2222")
        book3 = Book.objects.create(title="Book3", description="good", isbn="3333")
        book4 = Book.objects.create(title="Book4", description="good", isbn="4444")

        response = self.client.get(reverse("books:list"))

        for book in [book1, book2]:
            self.assertContains(response, book.title)

        response = self.client.get(reverse("books:list") + "?page=2")

        for book in [book3, book4]:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="good", isbn="1111")
        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))
        self.assertContains(response, book.title)
        self.assertContains(response, book.description)

    def test_search_books(self):
        book1 = Book.objects.create(title="Sport", description="good", isbn="1111")
        book2 = Book.objects.create(title="Guide", description="good", isbn="2222")
        book3 = Book.objects.create(title="Movie", description="good", isbn="3333")

        response = self.client.get(reverse("books:list") + "?q=sport")
        self.assertContains(response, book1.title)
        self.assertNotContains(response, book2.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=Guide")
        self.assertContains(response, book2.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book3.title)

        response = self.client.get(reverse("books:list") + "?q=Movie")
        self.assertContains(response, book3.title)
        self.assertNotContains(response, book1.title)
        self.assertNotContains(response, book2.title)


class BookReviewTestCase(TestCase):
    def test_add_review(self):
        pass  # 31 darsda
