from django.urls import path
from .api import BookListApi, BookCreateApi  # Ensure this import is valid

urlpatterns = [
    path('list/', BookListApi, name='book-list'),  # Ensure the trailing slash
    path('create', BookCreateApi , name = 'book-create'),
]
