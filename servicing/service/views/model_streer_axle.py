

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import ModelStreerAxle
from service.serializers import ModelStreerAxleSerializer


@api_view(["GET", "POST"])
def model_streer_axle_list_create(request):
    if request.method == "GET":
        model_streer_axles = ModelStreerAxle.objects.all()
        serializer = ModelStreerAxleSerializer(model_streer_axles, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ModelStreerAxleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def model_streer_axle_detail(request, id):
    model_streer_axle = get_object_or_404(ModelStreerAxle, id=id)
    serializer = ModelStreerAxleSerializer(model_streer_axle)
    return Response(serializer.data)

@api_view(["PUT"])
def model_streer_axle_update(request, id):
    model_streer_axle = get_object_or_404(ModelStreerAxle, id=id)
    serializer = ModelStreerAxleSerializer(
        instance = model_streer_axle,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def model_streer_axle_delete(request, id):
    model_streer_axle = get_object_or_404(ModelStreerAxle, id=id)
    model_streer_axle.delete()
    return Response(
        {"message": "model_streer_axle deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


