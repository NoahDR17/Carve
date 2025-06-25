from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Profile, ProgressStat
from .serializers import ProfileSerializer, ProgressStatSerializer

class ProfileDetail(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user.profile

class ProgressStatListCreate(generics.ListCreateAPIView):
    serializer_class = ProgressStatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProgressStat.objects.filter(user=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProgressStatDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProgressStatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ProgressStat.objects.filter(user=self.request.user)