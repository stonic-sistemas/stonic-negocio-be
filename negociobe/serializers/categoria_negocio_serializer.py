from rest_framework import serializers
from negociobe.models.categoria_negocio import CategoriaNegocio

class CategoriaNegocioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaNegocio
        fields = ('idcategorianegocio', 'nombre')