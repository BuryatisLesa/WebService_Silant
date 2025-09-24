

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.complaint import MethodRestoration
from service.serializers import MethodRestorationSerializer


@api_view(["GET", "POST"])
def method_restoration_list_create(request):
    if request.method == "GET":
        method_restorations = MethodRestoration.objects.all()
        serializer = MethodRestorationSerializer(method_restorations, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = MethodRestorationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["GET"])
def method_restoration_detail(request, id):
    method_restoration = get_object_or_404(MethodRestoration, id=id)
    serializer = MethodRestorationSerializer(method_restoration)
    return Response(serializer.data)

@api_view(["PUT"])
def method_restoration_update(request, id):
    method_restoration = get_object_or_404(MethodRestoration, id=id)
    serializer = MethodRestorationSerializer(
        instance = method_restoration,
        data=request.data,
        partial = True,
        )
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def method_restoration_delete(request, id):
    method_restoration = get_object_or_404(MethodRestoration, id=id)
    method_restoration.delete()
    return Response(
        {"message": "method_restoration deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)


