from django.contrib import admin
from service.models.mashine import (
    Machines,
    # Model_Machine,
    # Model_Engine,
    # Model_Drive_Axle,
    # Model_Stree_Axle,
    # Model_Transmission
)

# from service.models.service_company import Service_Company


admin.site.register(Machines)
