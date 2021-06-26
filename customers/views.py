from django.shortcuts import render

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

from .models import Transfer, Withdraw, Deposit, Contact
from .serializers import TransferSerializer, DepositSerializer, WithdrawSerializer, ContactSerializer

# Create your views here.

class TransferList(generics.ListCreateAPIView):
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

class TransferListAuth(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer

    def get_object(self):
        return self.request.user

class WithdrawList(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

class WithdrawListAuth(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer

    def get_object(self):
        return self.request.user

class DepositList(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class DepositListAuth(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

    def get_object(self):
        return self.request.user

class ContactList(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer