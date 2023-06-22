from rest_framework.generics import UpdateAPIView
from infrastructure.entities.models import Client
from infrastructure.serializers.client import  SerializerClientUpdate



class ClientUpdate(UpdateAPIView):
    """Actualizar un cliente."""
    serializer_class = SerializerClientUpdate

    def get_queryset(self):

        queryset = Client.objects.filter(is_active=True,  id=self.kwargs.get("pk", 0))
        return queryset
        
