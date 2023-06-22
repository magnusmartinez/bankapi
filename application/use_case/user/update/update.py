from rest_framework.generics import UpdateAPIView
from infrastructure.entities.models import User
from infrastructure.serializers.user import  SerializerUserUpdate



class UserUpdate(UpdateAPIView):
    """Actualizar un ususrio."""
    queryset = User.objects.filter(is_active=True)
    serializer_class = SerializerUserUpdate

