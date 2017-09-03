from rest_framework.response import Response
from Complaints.serializers import ComplaintSerializer
from rest_framework.decorators import api_view
from Complaints.models import Complaint
from rest_framework import status


@api_view(['GET', 'POST'])
def complaints_list(request):

    print(request.method)
    print("yo")
    if request.method == 'GET':

        products = Complaint.objects.all()
        serializer = ComplaintSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print (request.data)
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




