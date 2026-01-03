

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import Client
from service.serializers import ClientSerializer


@api_view(["GET", "POST"])
def client_list_create(request):
    """список клиентов и создание записи"""
    if request.method == "GET":
        model_engines = Client.objects.all()
        serializer = ClientSerializer(model_engines, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def client_detail(request, id):
    """подробности модели двигателя"""
    model_engine = get_object_or_404(Client, id=id)
    serializer = ClientSerializer(model_engine)
    return Response(serializer.data)

@api_view(["PUT"])
def client_update(request, id):
    """обновление данных о модели двигателя"""
    model_engine = get_object_or_404(Client, id=id)
    serializer = ClientSerializer(
        instance = model_engine,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def client_delete(request, id):
    """удаление запись модели двигателя"""
    model_engine = get_object_or_404(Client, id=id)
    model_engine.delete()
    return Response(
        {"message": "model_engine deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


