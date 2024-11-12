from rest_framework import serializers
from .models import DateTime

class DateTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DateTime
        fields = '__all__'