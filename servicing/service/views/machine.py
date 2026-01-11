
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated

from service.models.machine import Machine, Client

from service.serializers import (
    MachineSerializer,
    )

@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def machine_list_create(request):
    """получение машин и создание машины"""
    if request.method == "GET":
        user = request.user
        queryset = Machine.objects.none()
        if user.is_authenticated:
            # Проверка на доступ к записям через модель Client
            client_profile = Client.objects.filter(user = user).first()
            role = client_profile.role if client_profile else "None"

            if role == "manager" or user.is_staff:
                queryset = Machine.objects.all().order_by("-date_shipment_with_factory")
            else:
                queryset = Machine.objects.filter(client__user=user).order_by("-date_shipment_with_factory")
        else:
            # Получаем значение search
            search_query = request.query_params.get("search", None)

            # Фильтруем данные, если search_query есть
            if search_query:
                queryset = Machine.objects.filter(unique_machine_number__icontains=search_query).order_by("-date_shipment_with_factory")  

            else:
                queryset = Machine.objects.none()
            
        serializer = MachineSerializer(queryset, many=True)
        return Response(serializer.data)


    if request.method == "POST":
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def machine_detail(request, id):
    """подробности машины"""
    machine = get_object_or_404(Machine, id=id)
    serializer = MachineSerializer(machine)
    return Response(serializer.data)

@api_view(["PUT"])
def machine_update(request, id):
    """обновление данных о машине"""
    machine = get_object_or_404(Machine, id=id)
    serializer = MachineSerializer(instance=machine, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def machine_delete(request, id):
    """удаление записи машины"""
    machine = get_object_or_404(Machine, id=id)
    machine.delete()
    return Response(
        {"message": "Machine deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)