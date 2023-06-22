from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from application.use_case.client.create.create import ClientCreate
from application.use_case.client.update.update import ClientUpdate
from application.use_case.client.list.list_one import ClientListOne
from application.use_case.client.list.list_by_sucursal import ClientListBySucursal
from application.use_case.client.list.list import ClientList
from application.use_case.client.delete.delete import ClientDelete

urlpatterns = [
    path('client/create/', ClientCreate.as_view()),
    path('client/list/', ClientList.as_view()),
    path('client/list/<int:pk>', ClientListOne.as_view()),
    path('client/list/by/sucursal/<int:sucursal>', ClientListBySucursal.as_view()),
    path('client/update/<int:pk>', ClientUpdate.as_view()),
    path('client/delete/<int:pk>', ClientDelete.as_view())
]
