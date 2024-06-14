from django.urls import path
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('status/<str:pk>', views.status, name='status'),
]
