from rest_framework.generics import UpdateAPIView
from infrastructure.entities.models import Account
from infrastructure.serializers.account import  SerializerAccountUpdate



class AccountUpdate(UpdateAPIView):
    """Actualizar una cuenta."""
    serializer_class = SerializerAccountUpdate

    def get_queryset(self):

        queryset = Account.objects.filter(is_active=True,  id=self.kwargs.get("pk", 0))
        return queryset
        
