from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

from .serializers import BookSerializers,Books

@api_view(['GET'])
def api_index(request):
    
    book=Books.objects.all()
    serializer=BookSerializers(book,many=True)

    return Response(serializer.data)
