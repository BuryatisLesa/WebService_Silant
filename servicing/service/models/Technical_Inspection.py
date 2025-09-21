from django.db import models
from service.models.Service_Company import Service_Company
from service.models.Mashine import Machine

class Technical_Inspection(models.Model):
    type_TI = models.ForeignKey(
        "Type_TI",
        on_delete=models.CASCADE,
        related_name="technical_incpection"
        )
    
    date_service = models.DateTimeField(auto_now=True)

    running_hours = models.IntegerField(default=0)

    order = models.CharField(max_length=500)

    date_order = models.DateField()

    service_company = models.ForeignKey(
        Service_Company,
        on_delete=models.CASCADE,
        related_name="service_company")
    
    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="ti_by_machine")


class Type_TI(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()