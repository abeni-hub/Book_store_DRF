from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import BookModel
@api_view(['GET'])
@renderer_classes([JSONRenderer])  # Force JSON response
def BookListApi(request):
    # fetch from the database

    books = BookModel.objects.all()

    books = [
        {
            'name': book.name ,
            'author': book.author
        } for book in books]

    # send response
    return Response(books)


@api_view(['POST'])
def BookCreateApi(request):

    data = request.data

    name = data['name']
    author = data['author']

    BookModel(name = name, author = author).save()

    return Response({
        'message': 'Book Created'
    })