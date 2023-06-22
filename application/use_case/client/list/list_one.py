from rest_framework.generics import RetrieveAPIView
from infrastructure.entities.models import Client
from infrastructure.serializers.client import  SerializerClientListOne


 
class ClientListOne(RetrieveAPIView): 
    """Listar un cliente."""

    serializer_class = SerializerClientListOne

    def get_queryset(self):
        queryset = Client.objects.filter(is_active=True, id=self.kwargs.get("pk"))
        
        return queryset
        