from django.contrib import admin
from service.models.machine import (
    Machine,
    ModelMachine,
    ModelEngine,
    ModelDriveAxle,
    ModelSteerAxle,
    ModelTransmission,
    Client,
)

from service.models.technical_inspection import (
    TechnicalInspection,
)

from service.models.service_company import ServiceCompany


admin.site.register(Machine)
admin.site.register(ModelMachine)
admin.site.register(ModelEngine)
admin.site.register(ModelDriveAxle)
admin.site.register(ModelSteerAxle)
admin.site.register(ModelTransmission)
admin.site.register(ServiceCompany)
admin.site.register(Client)
admin.site.register(TechnicalInspection)
