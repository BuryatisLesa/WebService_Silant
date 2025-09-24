from django.urls import path
from service.views import machine

urlpatterns = [
    path("api/machines/", machine.machine_list_create, name="machine-list-create"),
    path("api/machines/<int:id>/", machine.machine_detail, name="machine"),
    path("api/machines/<int:id>/update/", machine.machine_update, name="machine-update"),  
    path("api/machines/<int:id>/delete/", machine.machine_delete, name="machine-delete"),
]
