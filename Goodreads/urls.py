from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Goodreads.views import landing_page, home_page

urlpatterns = [
    path("", landing_page, name="landing_page"),
    path("home/", home_page, name="home_page"),
    path("books/", include("book.urls")),
    path("users/", include("users.urls")),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)