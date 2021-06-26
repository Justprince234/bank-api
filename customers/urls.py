from django.urls import path


from .views import TransferList, DepositList, WithdrawList, ContactList, TransferListAuth, WithdrawListAuth, DepositListAuth

urlpatterns = [
    path('api/transferList/', TransferList.as_view()),
    path('api/transferlistauth/', TransferListAuth.as_view()),
    path('api/depositlist/', DepositList.as_view()),
    path('api/depositlistauth/', DepositListAuth.as_view()),
    path('api/withdrawlist/', WithdrawList.as_view()),
    path('api/withdrawlistauth/', WithdrawListAuth.as_view()),
    path('api/contactlist/', ContactList.as_view()),
]

