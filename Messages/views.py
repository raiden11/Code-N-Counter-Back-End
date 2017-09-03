from rest_framework.response import Response
from Messages.serializers import MessageSerializer
from rest_framework.decorators import api_view
from Messages.models import Message
from rest_framework import status


@api_view(['GET', 'POST'])
def messages_list(request):

    print ("yo")
    if request.method == 'GET':

        products = Message.objects.all()
        serializer = MessageSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print (request.data)
        serializer = MessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def message_user(request, pk):

    if request.method == 'GET':

        messages = Message.objects.filter(Rec=pk)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)


