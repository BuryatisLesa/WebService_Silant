from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.technical_inspection import TechnicalInspection
from service.models.machine import Machine, Client

from service.serializers import TechnicalInspectionSerializer



@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def technical_inspection_list_create(request):
    if request.method == "GET":
        # Получаем пользователя из токена (request.user)
        user = request.user
        queryset = TechnicalInspection.objects.none()
        
        if user.is_authenticated:
            # Проверка на доступ к записям через модель Client
            client_profile = Client.objects.filter(user = user).first()
            role = client_profile.role if client_profile else "None"

            if role == "manager" or user.is_staff:
                queryset = TechnicalInspection.objects.all().order_by("-date_service")
            else:
                # Фильтруем ТО: ищем записи, где клиент связан с этим пользователем
                # client__user — это путь через модель Client к модели User
                machines = Machine.objects.filter(client__user = user)
                queryset = TechnicalInspection.objects.filter(machine__in = machines).order_by("-date_service")
        serializer = TechnicalInspectionSerializer(queryset, many=True)
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
    """подробности ТО"""
    technical_inspection = get_object_or_404(TechnicalInspection, id=id)
    serializer = TechnicalInspectionSerializer(technical_inspection)
    return Response(serializer.data)


@api_view(["PUT", "PATCH"])
@permission_classes([IsAuthenticated])
def technical_inspection_update(request, id):
    """обновление ТО"""
    technical_inspection = get_object_or_404(
        TechnicalInspection,
        id=id,
        machine__client__user = request.user)
    
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
def techical_inspection_delete(request, id):
    """удаление ТО"""
    techical_inspection = get_object_or_404(TechnicalInspection, id=id)
    techical_inspection.delete()
    return Response(
        {"message": "Techincal inspection deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)

