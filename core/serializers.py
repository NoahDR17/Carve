from rest_framework import serializers
from .models import Profile, ProgressStat


class ProfileSerializer(serializers.ModelSerializer):
    bmi = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['id', 'bio', 'age', 'height_cm', 'weight_kg', 'profile_image', 'bmi']

    def get_bmi(self, obj):
        return obj.bmi()

class ProgressStatSerializer(serializers.ModelSerializer):
    bmi = serializers.SerializerMethodField()

    class Meta:
        model = ProgressStat
        fields = ['id', 'date', 'weight_kg', 'body_fat_percentage', 'notes', 'bmi']

    def get_bmi(self, obj):
        return obj.bmi()