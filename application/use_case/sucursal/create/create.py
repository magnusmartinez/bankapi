from rest_framework.generics import CreateAPIView
from infrastructure.entities.models import Sucursal
from infrastructure.serializers.sucursal import SerializerSucursalCreate


class SucursalCreate(CreateAPIView):  
    """Crear una sucursal de un banco"""
    
    serializer_class = SerializerSucursalCreate
