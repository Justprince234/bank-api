from django.db import models
from accounts.models import User
import uuid



# Create your models here.

def transaction_id():
       return str(uuid.uuid1())


class Withdraw(models.Model):
       from_account = models.CharField(max_length=50)
       amount = models.FloatField()
       transaction_id = models.CharField(default=transaction_id, unique=True, max_length=200)
       user_id = models.ForeignKey(User, on_delete=models.CASCADE)

       class Meta:
        verbose_name_plural = "Customer Withdrawals"

class Deposit(models.Model):
       amount = models.FloatField()
       to_account = models.CharField(max_length=50)
       transaction_id = models.CharField(default=transaction_id, unique=True, max_length=200)

       class Meta:
        verbose_name_plural = "Customer Deposits"

class Transfer(models.Model):
       to_account_number = models.CharField(max_length=50)
       to_account_available_bal = models.FloatField()
       to_account_name = models.CharField(max_length=100)
       transfer_amount = models.FloatField()
       from_account_available_bal = models.FloatField()
       transaction_id = models.CharField(default=transaction_id, unique=True, max_length=200)
       timestamp = models.DateTimeField(auto_now_add=True)
       user_id = models.ForeignKey(User, on_delete=models.CASCADE)

       class Meta:
              verbose_name_plural = "Customer Transfers"

       def __str__(self):
              return "{} was tranfered to {} from {}".format(self.amount, self.to_account, self.from_account)

class Contact(models.Model):
       name = models.CharField(max_length=200)
       email = models.EmailField()
       phone_number = models.CharField(max_length=20)
       query = models.TextField()

       class Meta:
        verbose_name_plural = "Contact Us"