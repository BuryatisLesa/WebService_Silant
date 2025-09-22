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


class MachineSerializer(serializers.Serializer):
    class Meta:
        model = Machine
        fields = "__all__"

class ModelEngineSerializer(serializers.Serializer):
    class Meta:
        model = ModelEngine
        fields = "__all__"

class ModelDriveAxleSerializer(serializers.Serializer):
    class Meta:
        model = ModelDriveAxle
        fields = "__all__"

class ModelMachineSerializer(serializers.Serializer):
    class Meta:
        model = ModelMachine
        fields = "__all__"

class ModelStreerAxleSerializer(serializers.Serializer):
    class Meta:
        model = ModelStreerAxle
        fields = "__all__"

class ModelStreerAxleSerializer(serializers.Serializer):
    class Meta:
        model = ModelTransmission
        fields = "__all__"

class ComplaintSerializer(serializers.Serializer):
    class Meta:
        model = Complaint
        fields = "__all__"

class FailedUnitSerializer(serializers.Serializer):
    class Meta:
        model = FailedUnit
        fields = "__all__"

class MethodRestorationSerializer(serializers.Serializer):
    class Meta:
        model = MethodRestoration
        fields = "__all__"

class ServiceCompanySerializer(serializers.Serializer):
    class Meta:
        model = ServiceCompany
        fields = "__all__"

class TechnicalInspectionSerializer(serializers.Serializer):
    class Meta:
        model = TechnicalInspection
        fields = "__all__"

class TypeTISerializer(serializers.Serializer):
    class Meta:
        model = TypeTI
        fields = "__all__"



