from django.db import models

from service.models.Mashine import Machine
from service.models.Service_Company import Service_Company


class Complaint(models.Model):

    date_failure = models.DateField()

    running_hours = models.IntegerField(default=0)

    failed_unit = models.ForeignKey(
        "Failed_Unit",
        on_delete=models.CASCADE,
        related_name="complaint_failed_unit"
    )
    
    description_failed = models.TextField()

    method_restoration = models.ForeignKey(
        "Method_Restoration",
        on_delete=models.CASCADE,
        related_name="complaint_method_restoration"
    )
    spare_parts_usage = models.CharField(max_length=500)

    date_restoration = models.DateField()

    time_stop_machine = date_restoration - date_failure

    machine = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name="complaint_machine"
    )

    service_company = models.ForeignKey(
        Service_Company,
        on_delete=models.CASCADE,
        related_name="complaint_service_company"
    )
    


class Failed_Unit(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()


class Method_Restoration(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()