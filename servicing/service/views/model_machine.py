

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import ModelMachine
from service.serializers import ModelMachineSerializer


@api_view(["GET", "POST"])
def model_machine_list_create(request):
    if request.method == "GET":
        model_machines = ModelMachine.objects.all()
        serializer = ModelMachineSerializer(model_machines, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ModelMachineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def model_machine_detail(request, id):
    model_machine = get_object_or_404(ModelMachine, id=id)
    serializer = ModelMachineSerializer(model_machine)
    return Response(serializer.data)

@api_view(["PUT"])
def model_machine_update(request, id):
    model_machine = get_object_or_404(ModelMachine, id=id)
    serializer = ModelMachineSerializer(
        instance = model_machine,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def model_machine_delete(request, id):
    model_machine = get_object_or_404(ModelMachine, id=id)
    model_machine.delete()
    return Response(
        {"message": "Model_machine deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


