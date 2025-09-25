from django.urls import path

# views app => service
from service.views import (
    machine,
    model_machine,
    model_engine,
    model_transmission,
    model_drive_axle,
    model_streer_axle,
    method_restoration,
    technical_inspection,
    type_TI,
    complaint,
    failed_unit,
    service_company
    )


urlpatterns = []

def add_urls(array: list) -> None:
    for url in array:
        urlpatterns.append(url)



url_machine = [
    path("api/machines/", machine.machine_list_create, name="machine-list-create"),
    path("api/machines/<int:id>/", machine.machine_detail, name="machine"),
    path("api/machines/<int:id>/update/", machine.machine_update, name="machine-update"),  
    path("api/machines/<int:id>/delete/", machine.machine_delete, name="machine-delete"),]


url_model_machine = [
    path(
        "api/model_machines/",
         model_machine.model_machine_list_create,
         name="model-machine-list-create"
         ),
    path(
        "api/model_machines/<int:id>/",
         model_machine.model_machine_detail,
         name="model-machine"
         ),
    path(
        "api/model_machines/<int:id>/update/",
         model_machine.model_machine_update,
         name="model-machine-update"
         ),
    path(
        "api/model_machines/<int:id>/delete/",
         model_machine.model_machine_delete,
         name="model-machine-delete"
         ),
]


url_model_engine = [
    path(
        "api/model_engine/",
        model_engine.model_engine_list_create,
        name="model-enignes-list-create"
    ),
    path(
        "api/model_engine/<int:id>/",
        model_engine.model_engine_detail,
        name="model-enigne"
    ),
    path(
        "api/model_engine/<int:id>/update/",
        model_engine.model_engine_update,
        name="model-enigne-update"
    ),
    path(
        "api/model_engine/<int:id>/delete/",
        model_engine.model_engine_delete,
        name="model-enigne-delete"
    ),
]

url_model_transmission = [
    path(
        "api/model_transmission/",
        model_transmission.model_transmission_list_create,
        name="model-transmissions-list-create",
    ),
    path(
        "api/model_transmission/<int:id>/",
        model_transmission.model_transmission_detail,
        name="model-transmission-detail",
    ),
    path(
        "api/model_transmission/<int:id>/update/",
        model_transmission.model_transmission_update,
        name="model-transmission-update",
    ),
    path(
        "api/model_transmission/<int:id>/delete/",
        model_transmission.model_transmission_delete,
        name="model-transmission-delete",
    ),
]

url_model_drive_axle = [
    path(
        "api/model_drive_axle/",
        model_drive_axle.model_drive_axle_list_create,
        name="model-drive-axle-list-create",
    ),
    path(
        "api/model_drive_axle/<int:id>/",
        model_drive_axle.model_drive_axle_detail,
        name="model-drive-axle",
    ),
    path(
        "api/model_drive_axle/<int:id>/update/",
        model_drive_axle.model_drive_axle_update,
        name="model-drive-axle-update",
    ),
    path(
        "api/model_drive_axle/<int:id>/delete/",
        model_drive_axle.model_drive_axle_delete,
        name="model-drive-axle-delete",
    ),
]

url_model_steer_axle = [
    path(
        "api/model_steer_axle/",
        model_streer_axle.model_streer_axle_list_create,
        name="model-steer-axle-list-create",
    ),
    path(
        "api/model_steer_axle/<int:id>/",
        model_streer_axle.model_streer_axle_detail,
        name="model-steer-axle",
    ),
    path(
        "api/model_steer_axle/<int:id>/update/",
        model_streer_axle.model_streer_axle_update,
        name="model-steer-axle-update",
    ),
    path(
        "api/model_steer_axle/<int:id>/delete/",
        model_streer_axle.model_streer_axle_delete,
        name="model-steer-axle-delete",
    ),
]

url_service_company = [
    path(
        "api/service_company/",
        service_company.service_company_list_create,
        name="service-company-list-create",
    ),
    path(
        "api/service_company/<int:id>/",
        service_company.service_company_detail,
        name="service-company",
    ),
    path(
        "api/service_company/<int:id>/update/",
        service_company.service_company_update,
        name="service-company-update",
    ),
    path(
        "api/service_company/<int:id>/delete/",
        service_company.service_company_delete,
        name="service-company-delete",
    ),
]

url_technical_inspection = [
    path(
        "api/technical_inspections/",
        technical_inspection.technical_inspection_list_create,
        name="technical-inspection-list-create",
    ),
    path(
        "api/technical_inspections/<int:id>/",
        technical_inspection.technical_inspection_detail,
        name="technical-inspection-detail",
    ),
    path(
        "api/technical_inspections/<int:id>/update/",
        technical_inspection.technical_inspection_update,
        name="technical-inspection-update",
    ),
    path(
        "api/technical_inspections/<int:id>/delete/",
        technical_inspection.techical_inspection_delete,
        name="technical-inspection-delete",
    ),
]

url_type_TI = [
    path(
        "api/type_technical_inspections/",
        type_TI.type_TI_list_create,
        name="type-TI-list-create",
    ),
    path(
        "api/type_technical_inspections/<int:id>/",
        type_TI.type_TI_detail,
        name="type-TI",
    ),
    path(
        "api/type_technical_inspections/<int:id>/update/",
        type_TI.type_TI_update,
        name="type-TI-update",
    ),
    path(
        "api/type_technical_inspections/<int:id>/delete/",
        type_TI.type_TI_delete,
        name="type-TI-delete",
    ),
]

url_complaint = [
    path(
        "api/complaints/",
        complaint.complaint_list_create,
        name="complaints-list-create",
    ),
    path(
        "api/complaints/<int:id>/",
        complaint.complaint_detail,
        name="complaint",
    ),
    path(
        "api/complaints/<int:id>/update/",
        complaint.complaint_update,
        name="complaints-update",
    ),
    path(
        "api/complaints/<int:id>/delete/",
        complaint.complaint_delete,
        name="complaints-delete",
    ),
]

url_failed_unit = [
    path(
        "api/failed_units/",
        failed_unit.failed_unit_list_create,
        name="failed-unit-list-create",
    ),
    path(
        "api/failed_units/<int:id>/",
        failed_unit.failed_unit_detail,
        name="failed-unit",
    ),
    path(
        "api/failed_units/<int:id>/update/",
        failed_unit.failed_unit_update,
        name="failed-unit-update",
    ),
    path(
        "api/failed_units/<int:id>/delete/",
        failed_unit.failed_unit_delete,
        name="failed-unit-delete",
    ),
]

url_method_restoration = [
    path(
        "api/method_restorations/",
        method_restoration.method_restoration_list_create,
        name="method-restoration-list-create",
    ),
    path(
        "api/method_restorations/<int:id>/",
        method_restoration.method_restoration_detail,
        name="method-restoration",
    ),
    path(
        "api/method_restorations/<int:id>/update/",
        method_restoration.method_restoration_update,
        name="method-restoration-update",
    ),
    path(
        "api/method_restorations/<int:id>/delete/",
        method_restoration.method_restoration_delete,
        name="method-restoration-delete",
    ),
]

add_urls(url_machine)
add_urls(url_model_machine)
add_urls(url_model_engine)
add_urls(url_model_transmission)
add_urls(url_model_drive_axle)
add_urls(url_model_steer_axle)
add_urls(url_service_company)
add_urls(url_technical_inspection)
add_urls(url_type_TI)
add_urls(url_complaint)
add_urls(url_failed_unit)
add_urls(url_method_restoration)