from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Client
from infrastructure.serializers.client import  SerializerClientBySucursal

 
class ClientListBySucursal(ListAPIView): 
    """Listar todos los clientes de una sucursal"""

    serializer_class = SerializerClientBySucursal
    lookup_field = "sucursal"

    def get_queryset(self):
        queryset = Client.objects.filter(is_active=True, sucursal=self.kwargs.get('sucursal', 0)).order_by("create_at")
        return queryset
        