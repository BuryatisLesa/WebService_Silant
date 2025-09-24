from django.contrib import admin
from service.models.machine import (
    Machine,
    ModelMachine,
    ModelEngine,
    ModelDriveAxle,
    ModelStreerAxle,
    ModelTransmission
)

from service.models.service_company import ServiceCompany


admin.site.register(Machine)
admin.site.register(ModelMachine)
admin.site.register(ModelEngine)
admin.site.register(ModelDriveAxle)
admin.site.register(ModelStreerAxle)
admin.site.register(ModelTransmission)
admin.site.register(ServiceCompany)
