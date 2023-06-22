from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Transfer, Account
from infrastructure.serializers.transfer import  SerializerTransferByAccount

 
class TransferListBySourceAccount(ListAPIView): 
    """Listar todas las transferencias de una cuenta (source_account)"""

    serializer_class = SerializerTransferByAccount
    lookup_field = "source_account"

    def get_queryset(self):

        source_account = Account.objects.get(number=self.kwargs.get('source_account'))
        
        queryset = Transfer.objects.filter(is_active=True, source_account=source_account).order_by("create_at")
        return queryset
        