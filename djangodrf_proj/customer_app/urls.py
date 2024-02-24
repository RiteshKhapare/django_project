from django.urls import path
from .views import task_details_api, task_api

urlpatterns = [
    path('v1/', task_api),
    path('v1/<int:pk>/', task_details_api)
]

