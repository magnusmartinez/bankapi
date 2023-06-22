from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Account
from infrastructure.serializers.account import  SerializerAccountByOwner

 
class AccountListByOwner(ListAPIView): 
    """Listar todos las cuentas de un cliente (Owner)"""

    serializer_class = SerializerAccountByOwner
    lookup_field = "owner"

    def get_queryset(self):
        queryset = Account.objects.filter(is_active=True, owner=self.kwargs.get('owner', 0)).order_by("create_at")
        return queryset
        