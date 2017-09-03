from rest_framework import serializers
from Facilities.models import Facility


class FacilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Facility
        fields = '__all__'


