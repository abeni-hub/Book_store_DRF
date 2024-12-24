from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import BookModel
from rest_framework import serializers

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
    price =  data['price']
    
    if price < 0 :
        return Response ({
            'message':'Price cannot be negative'
        })

    BookModel(name = name, author = author , price = price ).save()

    return Response({
        'message': 'Book Created'
    })
    
   
@api_view(['PPUT'])
def BookUpdateApi(request,id):
    data = request.data    
    
    book = BookModel.objects.get(id = id)
    
    book.name = data['data']
    book.author = data['author']


    book.save()
    
    return Response({
        'message': 'Book Updapted'
    })    
    
@api_view(['DELETE']) 
def BookDeleteApi(request):
       
    book = BookModel.objects.get( id = id)
    book.delete()
    
    return Response({
        'message':'Book Deleted'
    })