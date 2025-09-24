
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.complaint import Complaint
from service.serializers import ComplaintSerializer


@api_view(["GET", "POST"])
def complaint_list_create(request):
    if request.method == "GET":
        complaints = Complaint.objects.all()
        serializer = ComplaintSerializer(
            complaints,
            many= True,
        )
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ComplaintSerializer(
            data = request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                            )

@api_view(["GET"])
def complaint_detail(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    serializer = ComplaintSerializer(complaint)
    return Response(serializer.data)


@api_view(["PUT"])
def complaint_update(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    serializer = ComplaintSerializer(
        complaint,
        data=request.data,
        partial = True,
        )
    
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def complaint_delete(request, id):
    complaint = get_object_or_404(Complaint, id=id)
    complaint.delete()
    return Response(
        {"message": "Complaint deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)
