
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.complaint import Complaint
from service.models.machine import Client, Machine
from service.serializers import ComplaintSerializer


@api_view(["GET", "POST"])
@permission_classes([AllowAny])
def complaint_list_create(request):
    """Все заявки(рекламации) и создание заявки"""
    if request.method == "GET":
        # Получаем пользователя из токена (request.user)
        user = request.user
        queryset = Complaint.objects.none()
        if user.is_authenticated:

            client_profile = Client.objects.filter(user = user).first()
            role = client_profile.role if client_profile else "None"

            if role == "manager" or user.is_staff:
                queryset = Complaint.objects.all().order_by("-date_failure")
            else:
                machines = Machine.objects.filter(client__user = user)
                queryset = Complaint.objects.filter(machine__in = machines).order_by("-date_failure")
        else:
            # Если пользователь не авторизован, возвращаем пустой список или ошибку
            queryset = Complaint.objects.none()

        # Фильтруем ТО: ищем записи, где клиент связан с этим пользователем
        # client__user — это путь через модель Client к модели User
        serializer = ComplaintSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ComplaintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def complaint_detail(request, id):
    """подробности заявки"""
    complaint = get_object_or_404(Complaint, id=id)
    serializer = ComplaintSerializer(complaint)
    return Response(serializer.data)


@api_view(["PUT"])
def complaint_update(request, id):
    """обновление заявки"""
    complaint = get_object_or_404(Complaint, id=id)
    serializer = ComplaintSerializer(
        complaint,
        data=request.data,
        partial = True,
        )
    
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
            )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def complaint_delete(request, id):
    """удаление заявки"""
    complaint = get_object_or_404(Complaint, id=id)
    complaint.delete()
    return Response(
        {"message": "Complaint deleted successfully"},
        status=status.HTTP_204_NO_CONTENT)
