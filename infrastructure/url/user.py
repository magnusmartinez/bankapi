from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from application.use_case.user.create.create import UserCreate
from application.use_case.user.update.update import UserUpdate
from application.use_case.user.list.list_one import UserListOne
from application.use_case.user.list.list import UserList
from application.use_case.user.delete.delete import UserDelete
from application.use_case.user.login.login import UserLogin
from application.use_case.user.login.verify import CustomTokenVerifyView
# from application.use_case.user.export.export import ExcelDownloadView


urlpatterns = [
    path('user/create/', UserCreate.as_view()),
    path('user/list/', UserList.as_view()),
    path('user/list/<int:pk>', UserListOne.as_view()),
    path('user/update/<int:pk>', UserUpdate.as_view()),
    path('user/delete/<int:pk>', UserDelete.as_view()),

    path('user/login/', UserLogin.as_view()),
    # path('user/export/', ExcelDownloadView.as_view()),

    path('user/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/token/verify/', CustomTokenVerifyView.as_view(), name='token_verify'),
]
