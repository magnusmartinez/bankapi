from rest_framework.generics import ListAPIView
from infrastructure.entities.models import Account
from infrastructure.serializers.account import  SerializerAccountList


class AccountList(ListAPIView): 
    """Listar todos las cuentas."""
    queryset = Account.objects.filter(is_active=True).order_by("create_at")
    serializer_class = SerializerAccountList

