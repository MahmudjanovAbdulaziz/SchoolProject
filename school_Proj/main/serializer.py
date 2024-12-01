from rest_framework import serializers

from .models import *


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = "__all__"


class TeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = "__all__"


class School_cherecters_countSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_cherecters_count
        fields = "__all__"


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"


class Our_graduatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Our_graduates
        fields = "__all__"
