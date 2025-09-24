from rest_framework import serializers

#модели:
from service.models.machine import (
    Machine,
    ModelEngine,
    ModelDriveAxle,
    ModelMachine,
    ModelStreerAxle,
    ModelTransmission,
    )
from service.models.complaint import Complaint, FailedUnit, MethodRestoration
from service.models.service_company import ServiceCompany
from service.models.technical_inspection import TechnicalInspection, TypeTI


class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"

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

class ModelStreerAxleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelStreerAxle
        fields = "__all__"

class ModelTransmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelTransmission
        fields = "__all__"

class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
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

class TechnicalInspectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechnicalInspection
        fields = "__all__"

class TypeTISerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeTI
        fields = "__all__"



