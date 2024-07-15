from django.urls import path, include
from rest_framework import routers
from negociobe.api.NegocioViewSet import NegocioViewSet  # Asegúrate de la ruta correcta

router = routers.DefaultRouter()
router.register('api/negocios', NegocioViewSet, 'negocios')

urlpatterns = [
    path('', include(router.urls)),
]