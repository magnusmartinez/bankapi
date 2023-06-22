from django.urls import path

from application.use_case.transaction.create.create import TransactionCreate
# from application.use_case.transaction.update.update import TransactionUpdate
from application.use_case.transaction.list.list_one import TransactionListOne
from application.use_case.transaction.list.list_by_destination_account import TransactionListByDestinationAccount

from application.use_case.transaction.list.list import TransactionList
from application.use_case.transaction.delete.delete import TransactionDelete



urlpatterns = [
    path('transaction/create/', TransactionCreate.as_view()),
    path('transaction/list/', TransactionList.as_view()),
    path('transaction/list/<int:pk>', TransactionListOne.as_view()),
    path('transaction/list/by/account/<str:destination_account>', TransactionListByDestinationAccount.as_view()),
    # # path('transaction/update/<int:pk>', TransactionUpdate.as_view()),
    path('transaction/delete/<int:pk>', TransactionDelete.as_view()),

]
