from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Transaction, Account
from infrastructure.serializers.transaction import  SerializerTransactionByDestinationAccount

 
class TransactionListByDestinationAccount(ListAPIView): 
    """Listar todas las transacciones de una cuenta (destination_account.number)"""

    serializer_class = SerializerTransactionByDestinationAccount
    lookup_field = "destination_account"

    def get_queryset(self):

        destination_account = Account.objects.get(number=self.kwargs.get('destination_account'))
        
        queryset = Transaction.objects.filter(is_active=True, destination_account=destination_account).order_by("create_at")
        return queryset
        