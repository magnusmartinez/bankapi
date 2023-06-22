from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Client
from infrastructure.serializers.client import  SerializerClientList


class ClientList(ListAPIView): 
    """Listar todos los clientes."""
    queryset = Client.objects.filter(is_active=True).order_by("create_at")
    serializer_class = SerializerClientList

