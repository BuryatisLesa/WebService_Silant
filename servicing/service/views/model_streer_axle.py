

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import ModelSteerAxle
from service.serializers import ModelSteerAxleSerializer


@api_view(["GET", "POST"])
def model_streer_axle_list_create(request):
    """список модели управляемого моста и создание записи"""
    if request.method == "GET":
        model_streer_axles = ModelSteerAxle.objects.all()
        serializer = ModelSteerAxleSerializer(model_streer_axles, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ModelSteerAxleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def model_streer_axle_detail(request, id):
    """подробности управляемого моста"""
    model_streer_axle = get_object_or_404(ModelSteerAxle, id=id)
    serializer = ModelSteerAxleSerializer(model_streer_axle)
    return Response(serializer.data)

@api_view(["PUT"])
def model_streer_axle_update(request, id):
    """обновление данных управляемого моста"""
    model_streer_axle = get_object_or_404(ModelSteerAxle, id=id)
    serializer = ModelSteerAxleSerializer(
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
    """удаление записи управляемого моста"""
    model_streer_axle = get_object_or_404(ModelSteerAxle, id=id)
    model_streer_axle.delete()
    return Response(
        {"message": "model_streer_axle deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


