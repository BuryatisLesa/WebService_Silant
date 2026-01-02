from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.technical_inspection import TypeTI 
from service.serializers import TypeTISerializer

@api_view(["GET", "POST"])
def type_TI_list_create(request):
    if request.method == "GET":
        # Получаем данные из справочника видов ТО
        type_TIs = TypeTI.objects.all()
        serializer = TypeTISerializer(type_TIs, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = TypeTISerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def type_TI_detail(request, id):
    type_TI = get_object_or_404(TypeTI, id=id)
    serializer = TypeTISerializer(type_TI)
    return Response(serializer.data)

@api_view(["PUT"])
def type_TI_update(request, id):
    type_TI = get_object_or_404(TypeTI, id=id)
    serializer = TypeTISerializer(
        instance=type_TI,
        data=request.data,
        partial=True,
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def type_TI_delete(request, id):
    type_TI = get_object_or_404(TypeTI, id=id)
    type_TI.delete()
    return Response(
        {"message": "TypeTI deleted successfully"},
        status=status.HTTP_204_NO_CONTENT
    )
