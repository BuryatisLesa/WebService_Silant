

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import ModelTransmission
from service.serializers import ModelTransmissionSerializer


@api_view(["GET", "POST"])
def model_transmission_list_create(request):
    if request.method == "GET":
        model_transmissions = ModelTransmission.objects.all()
        serializer = ModelTransmissionSerializer(model_transmissions, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ModelTransmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def model_transmission_detail(request, id):
    model_transmission = get_object_or_404(ModelTransmission, id=id)
    serializer = ModelTransmissionSerializer(model_transmission)
    return Response(serializer.data)

@api_view(["PUT"])
def model_transmission_update(request, id):
    model_transmission = get_object_or_404(ModelTransmission, id=id)
    serializer = ModelTransmissionSerializer(
        instance = model_transmission,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def model_transmission_delete(request, id):
    model_transmission = get_object_or_404(ModelTransmission, id=id)
    model_transmission.delete()
    return Response(
        {"message": "model_transmission deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


