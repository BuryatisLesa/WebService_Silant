from django.db import models
from service.models.service_company import Service_Company


class Machine(models.Model):
    unique_machine_number = models.CharField(max_length=500, unique=True)

    model_machine = models.ForeignKey(
        "Model_Machine",
        on_delete=models.CASCADE,
        related_name="machines_by_model"
    )

    model_engine = models.ForeignKey(
        "Model_Engine",
        on_delete=models.CASCADE,
        related_name="machines_by_engine"
    )

    number_engine = models.CharField(max_length=500)

    model_transmission = models.ForeignKey(
        "Model_Transmission",
        on_delete=models.CASCADE,
        related_name="machines_by_transmission"
    )

    number_transmission = models.CharField(max_length=500)

    #Модель ведущего моста
    model_drive_axle = models.ForeignKey(
        "Model_Drive_Axle",
        on_delete=models.CASCADE,
        related_name="machines_by_drive_axle"
    )
    

    number_drive_axle = models.CharField(max_length=500)

    #Модель управляемого моста
    model_steer_axle = models.ForeignKey(
        "Model_Streer_Axle",
        on_delete=models.CASCADE,
        related_name="machines_by_drive_axle"
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
        Service_Company,
        on_delete=models.CASCADE,
        related_name="machines_by_service"
    )



#Справочники

class Model_Machine(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class Model_Engine(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class Model_Transmission(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class Model_Drive_Axle(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()

class Model_Streer_Axle(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()