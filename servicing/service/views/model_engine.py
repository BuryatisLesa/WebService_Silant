

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.machine import ModelEngine
from service.serializers import ModelEngineSerializer


@api_view(["GET", "POST"])
def model_engine_list_create(request):
    if request.method == "GET":
        model_engines = ModelEngine.objects.all()
        serializer = ModelEngineSerializer(model_engines, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ModelEngineSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def model_engine_detail(request, id):
    model_engine = get_object_or_404(ModelEngine, id=id)
    serializer = ModelEngineSerializer(model_engine)
    return Response(serializer.data)

@api_view(["PUT"])
def model_engine_update(request, id):
    model_engine = get_object_or_404(ModelEngine, id=id)
    serializer = ModelEngineSerializer(
        instance = model_engine,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def model_engine_delete(request, id):
    model_engine = get_object_or_404(ModelEngine, id=id)
    model_engine.delete()
    return Response(
        {"message": "model_engine deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


