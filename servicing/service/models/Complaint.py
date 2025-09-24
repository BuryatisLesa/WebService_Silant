from django.db import models

from service.models.machine import Machine
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

    @property
    def time_stop_mashine(self):
        return (self.date_restoration - self.date_failure).days
    


class FailedUnit(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()


class MethodRestoration(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()