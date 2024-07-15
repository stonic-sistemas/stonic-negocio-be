from rest_framework import viewsets, permissions
from negociobe.models import Negocio
from negociobe.serializers import NegocioSerializer

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = NegocioSerializer