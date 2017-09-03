from rest_framework.response import Response
from Facilities.serializers import FacilitySerializer
from Stores.serializers import StoreSerializer
from rest_framework.decorators import api_view
from Facilities.models import Facility
from rest_framework import status
from Stores.models import Store


@api_view(['GET', 'POST'])
def fac_list(request):

    if request.method == 'GET':

        products = Facility.objects.all()
        serializer = FacilitySerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = FacilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def fac_id(request, pk):

    try:
        part = Facility.objects.get(pk=pk)
    except Facility.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacilitySerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':

        serializer = FacilitySerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
# returns all facilities with id pk
def fac_cats(request, pk):

    facs = Facility.objects.filter(CKey=pk)
    if request.method == 'GET':

        serializer = FacilitySerializer(facs, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def fac_stores(request, pk):

    stores = Store.objects.filter(ParKey=pk)
    if request.method == 'GET':
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)







