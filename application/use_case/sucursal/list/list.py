from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Sucursal
from infrastructure.serializers.sucursal import  SerializerSucursalList


class SucursalList(ListAPIView): 
    """Listar todas las sucursales activas"""
    queryset = Sucursal.objects.filter(is_active=True).order_by("create_at")
    serializer_class = SerializerSucursalList

