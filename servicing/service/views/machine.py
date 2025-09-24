
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from service.models.machine import Machine

from service.serializers import (
    MachineSerializer,
    )

@api_view(["GET", "POST"])
def machine_list_create(request):
    if request.method == "GET":
        machines = Machine.objects.all()
        serializer = MachineSerializer(machines, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        serializer = MachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def machine_detail(request, id):
    machine = get_object_or_404(Machine, id=id)
    serializer = MachineSerializer(machine)
    return Response(serializer.data)

@api_view(["PUT"])
def machine_update(request, id):
    machine = get_object_or_404(Machine, id=id)
    serializer = MachineSerializer(instance=machine, data=request.data, partial=True)  
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def machine_delete(request, id):
    machine = get_object_or_404(Machine, id=id)
    machine.delete()
    return Response(
        {"message": "Machine deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)