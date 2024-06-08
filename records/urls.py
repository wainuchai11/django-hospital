from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PatientViewSet, DrugViewSet, TreatmentViewSet

router = DefaultRouter()
router.register(r'patients', PatientViewSet)
router.register(r'drugs', DrugViewSet)
router.register(r'treatments', TreatmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
