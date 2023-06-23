from django.urls import path

from application.use_case.sucursal.create.create import SucursalCreate
from application.use_case.sucursal.update.update import SucursalUpdate
from application.use_case.sucursal.list.list_one import SucursalListOne
from application.use_case.sucursal.list.list import SucursalList
# from application.use_case.sucursal.delete.delete import SucursalDelete



urlpatterns = [
    path('sucursal/create/', SucursalCreate.as_view()),
    path('sucursal/list/', SucursalList.as_view()),
    path('sucursal/list/<int:pk>', SucursalListOne.as_view()),
    path('sucursal/update/<int:pk>', SucursalUpdate.as_view()),
    # path('sucursal/delete/<int:pk>', SucursalDelete.as_view()),
]
