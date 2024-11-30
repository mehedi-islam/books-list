from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # Add this import

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    # Add a redirect from root to books
    path('', lambda request: redirect('books/')),
]