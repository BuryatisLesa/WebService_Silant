
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404

from service.models.complaint import Complaint
from service.serializers import ComplaintSerializer


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def complaint_list_create(request):
    """Все заявки(рекламации) и создание заявки"""
    if request.method == "GET":
        # Получаем пользователя из токена (request.user)
        user = request.user
        
        # Фильтруем ТО: ищем записи, где клиент связан с этим пользователем
        # client__user — это путь через модель Client к модели User
        queryset = Complaint.objects.filter(machine__client__user = user)
        serializer = ComplaintSerializer(queryset, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = ComplaintSerializer(
            data = request.data,
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED,
                            )

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
