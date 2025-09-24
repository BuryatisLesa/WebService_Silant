

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.complaint import FailedUnit
from service.serializers import FailedUnitSerializer


@api_view(["GET", "POST"])
def failed_unit_list_create(request):
    if request.method == "GET":
        failed_units = FailedUnit.objects.all()
        serializer = FailedUnitSerializer(failed_units, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = FailedUnitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def failed_unit_detail(request, id):
    failed_unit = get_object_or_404(FailedUnit, id=id)
    serializer = FailedUnitSerializer(failed_unit)
    return Response(serializer.data)

@api_view(["PUT"])
def failed_unit_update(request, id):
    failed_unit = get_object_or_404(FailedUnit, id=id)
    serializer = FailedUnitSerializer(
        instance = failed_unit,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def failed_unit_delete(request, id):
    failed_unit = get_object_or_404(FailedUnit, id=id)
    failed_unit.delete()
    return Response(
        {"message": "failed_unit deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


