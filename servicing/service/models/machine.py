from django.db import models
from service.models.service_company import ServiceCompany
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_user_client_profile(sender, instance, created, **kwargs):
    """
    Сигнал срабатывает после сохранения User.
    created = True, если пользователь только что создан.
    """
    if created:
        # Создаем запись в таблице Client и привязываем её к новому User
        # По умолчанию роль будет "client"
        Client.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_client_profile(sender, instance, **kwargs):
    if hasattr(instance, 'client_profile'):
        for client in instance.client_profile.all():
            client.save()


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
        "ModelSteerAxle",
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
    client = models.ForeignKey('Client', on_delete=models.CASCADE, related_name='clients_machine')
    service_company = models.ForeignKey(
        ServiceCompany,
        on_delete=models.CASCADE,
        related_name="machines"
    )

    def __str__(self):
        return f"{self.model_machine.name} (№ {self.unique_machine_number})"



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

class ModelSteerAxle(models.Model):
    name = models.CharField(max_length=500)
    descriptions = models.TextField()


class Client(models.Model):
    class RoleChoices(models.TextChoices):
        CLIENT = "client", "Клиент"
        SERVICE_COMPANY = "service_company", "Сервисная компания"
        MANAGER = "manager", "Менеджер"

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_profile')
    
    role = models.CharField(
        max_length=20,
        choices=RoleChoices.choices,
        default=RoleChoices.CLIENT,
        verbose_name="Роль"
    )

    def __str__(self):
        return f"{self.user.username} ({self.get_role_display()})"