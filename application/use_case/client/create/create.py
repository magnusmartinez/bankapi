from rest_framework.generics import CreateAPIView
from infrastructure.entities.models import Client
from infrastructure.serializers.client import SerializerClientCreate


class ClientCreate(CreateAPIView):  
    """Crear un cliente del banco"""

    serializer_class = SerializerClientCreate
