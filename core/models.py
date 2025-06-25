from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField(blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    height_cm = models.FloatField(null=True, blank=True)
    weight_kg = models.FloatField(null=True, blank=True)
    profile_image = models.ImageField(upload_to='profiles/', null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def bmi(self):
        if self.height_cm and self.weight_kg:
            height_m = self.height_cm / 100
            return round(self.weight_kg / (height_m ** 2), 2)
        return None

class ProgressStat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='progress_stats')
    date = models.DateField(auto_now_add=True)
    weight_kg = models.FloatField()
    body_fat_percentage = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def bmi(self):
        profile = self.user.profile
        if profile.height_cm:
            height_m = profile.height_cm / 100
            return round(self.weight_kg / (height_m ** 2), 2)
        return None

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.weight_kg}kg"