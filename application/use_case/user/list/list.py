from rest_framework.generics import ListAPIView
from infrastructure.entities.models import User
from infrastructure.serializers.user import  SerializerUserList


 
class UserList(ListAPIView): 
    """Lista todos los usuarios activos"""
    queryset = User.objects.filter(is_active=True).order_by("id")
    serializer_class = SerializerUserList
