from rest_framework.generics import CreateAPIView
from infrastructure.serializers.user import SerializerUserCreate
from rest_framework.permissions import AllowAny


class UserCreate(CreateAPIView):  
    """Crear un nuevo usuario"""
    permission_classes = [AllowAny]
    serializer_class = SerializerUserCreate
    