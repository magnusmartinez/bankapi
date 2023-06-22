from django.urls import path

from application.use_case.transfer.create.create import TransferCreate
# from application.use_case.transfer.update.update import TransferUpdate
from application.use_case.transfer.list.list_one import TransferListOne
from application.use_case.transfer.list.list_by_source_account import TransferListBySourceAccount
from application.use_case.transfer.list.list_by_accounts import TransferListByAccounts
from application.use_case.transfer.list.list import TransferList
from application.use_case.transfer.delete.delete import TransferDelete



urlpatterns = [
    path('transfer/create/', TransferCreate.as_view()),
    path('transfer/list/', TransferList.as_view()),
    path('transfer/list/<int:pk>', TransferListOne.as_view()),
    path('transfer/list/by/account/<str:source_account>', TransferListBySourceAccount.as_view()),
    path('transfer/list/by/accounts/<str:source_account>/<str:destination_account>', TransferListByAccounts.as_view()),
    # path('transfer/update/<int:pk>', TransferUpdate.as_view()),
    path('transfer/delete/<int:pk>', TransferDelete.as_view()),

]
