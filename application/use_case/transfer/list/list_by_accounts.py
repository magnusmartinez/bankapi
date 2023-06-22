from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Transfer, Account
from infrastructure.serializers.transfer import  SerializerTransferByAccounts

 
class TransferListByAccounts(ListAPIView): 
    """Listar todas las transferencias realizadas entre cuentas (source_account) y (destination_account)"""

    serializer_class = SerializerTransferByAccounts
    lookup_field = "source_account"

    def get_queryset(self):

        source_account = Account.objects.get(number=self.kwargs.get('source_account', 0))
        destination_account = Account.objects.get(number=self.kwargs.get('destination_account', 0))
        
        queryset = Transfer.objects.filter(is_active=True, source_account=source_account, destination_account=destination_account).order_by("create_at")
   
        return queryset
        