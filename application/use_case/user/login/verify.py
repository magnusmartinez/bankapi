from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenVerifyView

class CustomTokenVerifyView(TokenVerifyView):
    permission_classes = [AllowAny]
