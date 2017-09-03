from rest_framework.response import Response
from Stores.serializers import StoreSerializer
from rest_framework.decorators import api_view
from Stores.models import Store
from rest_framework import status


@api_view(['GET', 'POST'])
def stores_list(request):

    if request.method == 'GET':

        products = Store.objects.all()
        serializer = StoreSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def stores_id(request, pk):

    try:
        part = Store.objects.get(pk=pk)
    except Store.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StoreSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':

        serializer = StoreSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



