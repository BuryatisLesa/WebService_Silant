

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.technical_inspection import TechnicalInspection

from service.serializers import TechnicalInspectionSerializer



@api_view(["GET", "POST"])
def technical_inspection_list_create(request):
    if request.method == "GET":
        technical_inspections = TechnicalInspection.objects.all()
        serializer = TechnicalInspectionSerializer(
            technical_inspections,
            many=True)
        
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = TechnicalInspectionSerializer(
            data = request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def technical_inspection_detail(request, id):
    technical_inspection = get_object_or_404(TechnicalInspection, id=id)
    serializer = TechnicalInspectionSerializer(technical_inspection)
    return Response(serializer.data)


@api_view(["PUT"])
def technical_inspection_update(request, id):
    technical_inspection = get_object_or_404(TechnicalInspection, id=id)
    serializer = TechnicalInspectionSerializer(
        instance = technical_inspection,
        data = request.data,
        partial= True, 
    )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["DELETE"])
def techical_inspection_delete(requset, id):
    techical_inspection = get_object_or_404(TechnicalInspection, id=id)
    techical_inspection.delete()
    return Response(
        {"message": "Techincal inspection deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)

