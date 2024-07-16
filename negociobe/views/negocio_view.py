from negociobe.models.negocio import Negocio
from negociobe.serializers.negocio_serializer import NegocioSerializer, CreateNegocioSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from django.db import connection

class NegocioViewSet(viewsets.ModelViewSet):
    queryset = Negocio.objects.all()
    serializer_class =NegocioSerializer

class CreateNegocioView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateNegocioSerializer(data=request.data)
        if serializer.is_valid():
            p_idusuario = serializer.validated_data['idusuario']
            p_nombrenegocio = serializer.validated_data['nombrenegocio']
            p_telefono = serializer.validated_data['telefono']
            p_idtiponegocio = serializer.validated_data['idtiponegocio']
            p_ruc = serializer.validated_data['ruc']

            with connection.cursor() as cursor:
                cursor.callproc('gen_man_negocio_ins', [
                    p_idusuario, p_nombrenegocio, p_telefono, p_idtiponegocio, p_ruc
                ])
                result = cursor.fetchone()

            p_message, p_code = result

            if p_code == 1:
                return Response({"message": p_message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": p_message}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
