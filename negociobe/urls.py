from django.urls import path, include
from negociobe.views.negocio_view import CreateNegocioView
from rest_framework.routers import DefaultRouter
from negociobe.views.negocio_view import NegocioViewSet

router = DefaultRouter()
router.register(r'api/negocios', NegocioViewSet, basename='negocios')

urlpatterns = [
    path('', include(router.urls)),
    path('create_negocio/', CreateNegocioView.as_view(), name='create-negocio'),
]