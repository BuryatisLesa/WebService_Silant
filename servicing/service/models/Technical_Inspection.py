from django.db import models
from service.models.service_company import ServiceCompany
from service.models.mashine import Machine


class TechnicalInspection(models.Model):
    type_ti = models.ForeignKey(
        "TypeTI",
        on_delete=models.CASCADE,
        related_name="technical_inspections"
    )

    date_service = models.DateField()

    running_hours = models.IntegerField(default=0)

    order = models.CharField(max_length=500)

    date_order = models.DateField()

    service_company = models.ForeignKey(
        ServiceCompany,
        on_delete=models.CASCADE,
        related_name="technical_inspections"
    )

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="technical_inspections"
    )


class TypeTI(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()
