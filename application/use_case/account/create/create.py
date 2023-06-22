from rest_framework.generics import CreateAPIView
from infrastructure.entities.models import Account
from infrastructure.serializers.account import SerializerAccountCreate


class AccountCreate(CreateAPIView):  
    """Crear una cuenta en el banco"""

    serializer_class = SerializerAccountCreate
