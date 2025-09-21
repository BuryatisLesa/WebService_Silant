from django.contrib import admin
from service.models.Mashine import (
    Machine,
    Model_Machine,
    Model_Engine,
    Model_Drive_Axle,
    Model_Streer_Axle,
    Model_Transmission
)

from service.models.Service_Company import Service_Company


admin.site.register(Machine)
admin.site.register(Model_Machine)
admin.site.register(Model_Engine)
admin.site.register(Model_Drive_Axle)
admin.site.register(Model_Streer_Axle)
admin.site.register(Model_Transmission)
admin.site.register(Service_Company)
