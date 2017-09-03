from rest_framework.response import Response
from Users.serializers import UserSerializer
from rest_framework.decorators import api_view
from Users.models import User
from rest_framework import status

import math


@api_view(['GET', 'POST'])
def users_list(request):

    if request.method == 'GET':

        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def users_id(request, pk):

    try:
        part = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(part)
        return Response(serializer.data)

    elif request.method == 'PATCH':

        serializer = UserSerializer(part, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(part, request.data)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':

        part.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def users_nearby(request):

    if request.method == 'POST':
        users = []
        lat = request.data.get("Latitude")
        long = request.data.get("Longitude")

        for user in User.objects.all():

            dt = math.sqrt((float(lat)-user.Latitude)*(float(lat)-user.Latitude) + (float(long)-user.Longitude)*(float(long)-user.Longitude))
            if dt <= 2:
                users.append(user)

        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)





