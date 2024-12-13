from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer

@api_view(['GET'])
@renderer_classes([JSONRenderer])  # Force JSON response
def BookListApi(request):
    books = [
        {
            'name': 'The Alchemist',
            'author': 'Paulo Coelho',
        },
        {
            'name': 'The Monk who Sold',
            'author': 'Robin Sharma',
        },
        {
            'name': 'The 5 AM Club',
            'author': 'Robin Sharma',
        }
    ]
    return Response(books)
