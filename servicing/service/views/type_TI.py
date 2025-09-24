

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.technical_inspection import TechnicalInspection
from service.serializers import TechnicalInspectionSerializer


@api_view(["GET", "POST"])
def type_TI_list_create(request):
    if request.method == "GET":
        type_TIs = TechnicalInspection.objects.all()
        serializer = TechnicalInspectionSerializer(type_TIs, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = TechnicalInspectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def type_TI_detail(request, id):
    type_TI = get_object_or_404(TechnicalInspection, id=id)
    serializer = TechnicalInspectionSerializer(type_TI)
    return Response(serializer.data)

@api_view(["PUT"])
def type_TI_update(request, id):
    type_TI = get_object_or_404(TechnicalInspection, id=id)
    serializer = TechnicalInspectionSerializer(
        instance = type_TI,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def type_TI_delete(request, id):
    type_TI = get_object_or_404(TechnicalInspection, id=id)
    type_TI.delete()
    return Response(
        {"message": "type_TI deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


