from django.urls import path
from .api import BookListApi  # Ensure this import is valid

urlpatterns = [
    path('list/', BookListApi, name='book-list'),  # Ensure the trailing slash
]
