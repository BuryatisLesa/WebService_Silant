from rest_framework import serializers

#модели:
from service.models.machine import (
    Machine,
    ModelEngine,
    ModelDriveAxle,
    ModelMachine,
    ModelSteerAxle,
    ModelTransmission,
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

class MachineSerializer(serializers.ModelSerializer):

    model_machine = ModelMachineSerializer()
    model_engine = ModelEngineSerializer()
    model_transmission = ModelTransmissionSerializer()
    model_drive_axle = ModelDriveAxleSerializer()
    model_steer_axle = ModelSteerAxleSerializer()
    service_company = ServiceCompanySerializer()

    class Meta:
        model = Machine
        fields = "__all__"
        # позволяет изменять и создавать записи
        depth = 1

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
            'type_ti_info', 'service_company_info', 'machine_info' # Поля для ЧТЕНИЯ
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


