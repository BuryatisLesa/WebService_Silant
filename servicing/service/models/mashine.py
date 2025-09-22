from django.db import models
from service.models.service_company import ServiceCompany


class Machine(models.Model):
    unique_machine_number = models.CharField(max_length=500, unique=True)

    model_machine = models.ForeignKey(
        "ModelMachine",
        on_delete=models.CASCADE,
        related_name="machines"
    )

    model_engine = models.ForeignKey(
        "ModelEngine",
        on_delete=models.CASCADE,
        related_name="machines"
    )

    number_engine = models.CharField(max_length=500)

    model_transmission = models.ForeignKey(
        "ModelTransmission",
        on_delete=models.CASCADE,
        related_name="machines"
    )

    number_transmission = models.CharField(max_length=500)

    #Модель ведущего моста
    model_drive_axle = models.ForeignKey(
        "ModelDriveAxle",
        on_delete=models.CASCADE,
        related_name="machines"
    )
    

    number_drive_axle = models.CharField(max_length=500)

    #Модель управляемого моста
    model_steer_axle = models.ForeignKey(
        "ModelStreerAxle",
        on_delete=models.CASCADE,
        related_name="machines"
    )

    number_steer_axle = models.CharField(max_length=500)

    number_supply_contract = models.CharField(max_length=500)

    date_shipment_with_factory = models.DateTimeField(auto_now_add=True)

    #Грузополучатель
    cargo_recipient = models.CharField(max_length=500)

    delivery_address = models.CharField(max_length=1000)

    configuration = models.CharField(max_length=500)

    client = models.CharField(max_length=500)

    service_company = models.ForeignKey(
        ServiceCompany,
        on_delete=models.CASCADE,
        related_name="machines"
    )



#Справочники

class ModelMachine(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class ModelEngine(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class ModelTransmission(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class ModelDriveAxle(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class ModelStreerAxle(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()