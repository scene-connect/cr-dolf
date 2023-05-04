from rest_framework import serializers

from .models import EPC, Ward


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = "__all__"


class EPCSerializer(serializers.ModelSerializer):
    ward = WardSerializer()

    class Meta:
        model = EPC
        fields = "__all__"
