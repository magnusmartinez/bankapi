from rest_framework.generics import RetrieveAPIView
from infrastructure.entities.models import Account
from infrastructure.serializers.account import  SerializerAccountListOne


 
class AccountListOne(RetrieveAPIView): 
    """Listar un cliente."""

    serializer_class = SerializerAccountListOne

    def get_queryset(self):
        queryset = Account.objects.filter(is_active=True, id=self.kwargs.get("pk"))
        
        return queryset
        