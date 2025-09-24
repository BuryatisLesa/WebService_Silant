
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework import status

from service.models.service_company import ServiceCompany

from service.serializers import ServiceCompanySerializer


@api_view(["GET", "POST"])
def service_company_list_create(request):
    if request.method == "GET":
        service_companies = ServiceCompany.objects.all()
        serializer = ServiceCompanySerializer(service_companies, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ServiceCompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
def service_company_detail(request, id):
    service_company = get_object_or_404(ServiceCompany, id=id)
    serializer = ServiceCompanySerializer(service_company)
    return Response(serializer.data)


@api_view(["PUT"])
def service_company_update(request, id):
    service_company = get_object_or_404(ServiceCompany, id=id)
    serializer = ServiceCompanySerializer(
        instance=service_company,
        data = request.data,
        partial = True,
        )
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def service_company_delete(request, id):
    service_company = get_object_or_404(ServiceCompany, id=id)
    service_company.delete()
    return Response(
        {"message": "Service_Company deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)