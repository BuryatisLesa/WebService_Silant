from django.db import models

from service.models.mashine import Machine
from service.models.service_company import ServiceCompany


class Complaint(models.Model):

    date_failure = models.DateField()

    running_hours = models.IntegerField(default=0)

    failed_unit = models.ForeignKey(
        "FailedUnit",
        on_delete=models.CASCADE,
        related_name="complaint"
    )
    
    description_failed = models.TextField()

    method_restoration = models.ForeignKey(
        "MethodRestoration",
        on_delete=models.CASCADE,
        related_name="complaint"
    )
    spare_parts_usage = models.CharField(max_length=500)

    date_restoration = models.DateField()

    time_stop_machine = date_restoration - date_failure

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="complaint"
    )

    service_company = models.ForeignKey(
        ServiceCompany,
        on_delete=models.CASCADE,
        related_name="complaint"
    )
    


class FailedUnit(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()


class MethodRestoration(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()