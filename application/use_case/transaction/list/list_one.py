from rest_framework.generics import RetrieveAPIView
from infrastructure.entities.models import Transaction
from infrastructure.serializers.transaction import  SerializerTransactionListOne


 
class TransactionListOne(RetrieveAPIView): 
    """Listar una transacción"""

    serializer_class = SerializerTransactionListOne

    def get_queryset(self):
        queryset = Transaction.objects.filter(is_active=True, id=self.kwargs.get("pk"))
        
        return queryset
        