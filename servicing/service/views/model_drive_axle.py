

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import ModelDriveAxle
from service.serializers import ModelDriveAxleSerializer


@api_view(["GET", "POST"])
def model_drive_axle_list_create(request):
    if request.method == "GET":
        model_drive_axles = ModelDriveAxle.objects.all()
        serializer = ModelDriveAxleSerializer(model_drive_axles, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ModelDriveAxleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def model_drive_axle_detail(request, id):
    model_drive_axle = get_object_or_404(ModelDriveAxle, id=id)
    serializer = ModelDriveAxleSerializer(model_drive_axle)
    return Response(serializer.data)

@api_view(["PUT"])
def model_drive_axle_update(request, id):
    model_drive_axle = get_object_or_404(ModelDriveAxle, id=id)
    serializer = ModelDriveAxleSerializer(
        instance = model_drive_axle,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def model_drive_axle_delete(request, id):
    model_drive_axle = get_object_or_404(ModelDriveAxle, id=id)
    model_drive_axle.delete()
    return Response(
        {"message": "model_drive_axle deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


