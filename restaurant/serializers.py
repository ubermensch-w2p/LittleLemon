from rest_framework import serializers

from .models import Booking, Menu


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Menu


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Booking
