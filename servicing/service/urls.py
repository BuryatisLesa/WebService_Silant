from django.urls import path
from service.views import machine

urlpatterns = [
    path("api/machines/", machine.machine_list_create, name="machine-list-create"),
    path("api/machines/<int:pk>/", machine.machine_detail, name="machine"),
    path("api/machines/<int:pk>/update/", machine.machine_update, name="machine-update"),  
    path("api/machines/<int:pk>/delete/", machine.machine_delete, name="machine-delete"),
]
