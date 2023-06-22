from django.urls import path

from application.use_case.account.create.create import AccountCreate
from application.use_case.account.update.update import AccountUpdate
from application.use_case.account.list.list_one import AccountListOne
from application.use_case.account.list.list_by_owner import AccountListByOwner
from application.use_case.account.list.list import AccountList
from application.use_case.account.delete.delete import AccountDelete



urlpatterns = [
    path('account/create/', AccountCreate.as_view()),
    path('account/list/', AccountList.as_view()),
    path('account/list/<int:pk>', AccountListOne.as_view()),
    path('account/list/by/owner/<int:owner>', AccountListByOwner.as_view()),
    path('account/update/<int:pk>', AccountUpdate.as_view()),
    path('account/delete/<int:pk>', AccountDelete.as_view()),

]
