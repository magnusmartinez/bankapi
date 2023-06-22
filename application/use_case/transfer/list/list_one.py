from rest_framework.generics import RetrieveAPIView
from infrastructure.entities.models import Transfer
from infrastructure.serializers.transfer import  SerializerTransferListOne


 
class TransferListOne(RetrieveAPIView): 
    """Listar una transferencia"""

    serializer_class = SerializerTransferListOne

    def get_queryset(self):
        queryset = Transfer.objects.filter(is_active=True, id=self.kwargs.get("pk"))
        
        return queryset
        