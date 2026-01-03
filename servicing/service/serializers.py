from rest_framework import serializers

#модели:
from service.models.machine import (
    Machine,
    ModelEngine,
    ModelDriveAxle,
    ModelMachine,
    ModelSteerAxle,
    ModelTransmission,
    Client,
    )

from service.models.complaint import Complaint, FailedUnit, MethodRestoration
from service.models.service_company import ServiceCompany
from service.models.technical_inspection import TechnicalInspection, TypeTI

class ModelEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelEngine
        fields = "__all__"

class ModelDriveAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelDriveAxle
        fields = "__all__"

class ModelMachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelMachine
        fields = "__all__"

class ModelSteerAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelSteerAxle
        fields = "__all__"

class ModelTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTransmission
        fields = "__all__"

class FailedUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = FailedUnit
        fields = "__all__"

class MethodRestorationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MethodRestoration
        fields = "__all__"

class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = "__all__"

class TypeTISerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTI
        fields = "__all__"

class ClientSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Client
        fields = "__all__"

class MachineSerializer(serializers.ModelSerializer):
    # Поля для ОТОБРАЖЕНИЯ (только чтение)
    model_machine_info = ModelMachineSerializer(source='model_machine', read_only=True)
    model_engine_info = ModelEngineSerializer(source='model_engine', read_only=True)
    model_transmission_info = ModelTransmissionSerializer(source='model_transmission', read_only=True)
    model_drive_axle_info = ModelDriveAxleSerializer(source='model_drive_axle', read_only=True)
    model_steer_axle_info = ModelSteerAxleSerializer(source='model_steer_axle', read_only=True)
    service_company_info = ServiceCompanySerializer(source='service_company', read_only=True)
    client_info = ClientSerializer(source="client", read_only=True)

    class Meta:
        model = Machine
        # Указываем все поля. Оригинальные поля (без _info) будут принимать ID при записи.
        fields = [
            'id', 'unique_machine_number', 'number_engine', 'number_transmission', 
            'number_drive_axle', 'number_steer_axle', 'number_supply_contract', 
            'date_shipment_with_factory', 'cargo_recipient', 'delivery_address', 
            'configuration', 'client', 'service_company', 'model_machine', 
            'model_engine', 'model_transmission', 'model_drive_axle', 'model_steer_axle',
            # Информационные поля
            'model_machine_info', 'model_engine_info', 'model_transmission_info',
            'model_drive_axle_info', 'model_steer_axle_info', 'service_company_info', 'client_info',
        ]


class TechnicalInspectionSerializer(serializers.ModelSerializer):
    # Поля для ОТОБРАЖЕНИЯ (read_only=True)
    # Эти данные будут приходить в React для показа в таблице
    type_ti_info = TypeTISerializer(source='type_ti', read_only=True)
    service_company_info = ServiceCompanySerializer(source='service_company', read_only=True)
    machine_info = MachineSerializer(source='machine', read_only=True)

    class Meta:
        model = TechnicalInspection
        fields = [
            'id', 'date_service', 'running_hours', 'order', 'date_order',
            'type_ti', 'service_company', 'machine', # Поля для ЗАПИСИ (принимают ID)
            'type_ti_info', 'service_company_info', 'machine_info',  # Поля для ЧТЕНИЯ
        ]


class ComplaintSerializer(serializers.ModelSerializer):
    time_stop = serializers.ReadOnlyField()
    failed_unit_info = FailedUnitSerializer(source='failed_unit', read_only=True)
    method_restoration_info = MethodRestorationSerializer(source='method_restoration', read_only=True)
    machine_info = MachineSerializer(source='machine', read_only=True)
    service_company_info = ServiceCompanySerializer(source='service_company', read_only=True)

    class Meta:
        model = Complaint
        fields = [
            'id', 'date_failure', 'running_hours', 'description_failed', 
            'spare_parts_usage', 'date_restoration', 'time_stop',
            'failed_unit', 'method_restoration', 'machine', 'service_company', # Для ЗАПИСИ (ID)
            'failed_unit_info', 'method_restoration_info', 'machine_info', 'service_company_info' # Для ЧТЕНИЯ
        ]


