from django.contrib import admin
from django.urls import path
from .views import CreatePacientView, IndexView, EditPatientView, PageNotFoundView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("pacient/", CreatePacientView.as_view(), name="pacient"),
    path('patient/edit/<int:id>/', EditPatientView.as_view(), name='edit_patient'),
    path('not_found/', PageNotFoundView.as_view(), name='not_found'),
]