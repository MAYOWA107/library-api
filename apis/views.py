from django.shortcuts import render

from rest_framework import generics
from books.models import Book

from .serializers import BookSerializer


class BooksApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

