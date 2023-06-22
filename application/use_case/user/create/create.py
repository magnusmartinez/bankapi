from rest_framework.generics import CreateAPIView
from infrastructure.serializers.user import SerializerUserCreate


class UserCreate(CreateAPIView):  
    """Crear un nuevo usuario"""

    serializer_class = SerializerUserCreate
