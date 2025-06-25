from django.urls import path
from .views import (
    ProfileDetail,
    ProgressStatListCreate,
    ProgressStatDetail,
)
urlpatterns = [
    path('profile/', ProfileDetail.as_view(), name='user-profile'),
    path('progress/', ProgressStatListCreate.as_view(), name='progress-list'),
    path('progress/<int:pk>/', ProgressStatDetail.as_view(), name='progress-detail'),
]