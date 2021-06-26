from django.contrib import admin

from .models import  Transfer, Withdraw, Deposit, Contact

# Register your models here.

admin.site.site_header = 'Deunion Reserve'
admin.site.site_title = 'Deunion Reserve'
admin.site.index_title = 'Deunion Reserve Bank Admin'

class TransferAdmin(admin.ModelAdmin):
  list_display = ('id', 'to_account_number', 'to_account_name', 'transfer_amount','transaction_id')
  list_display_links = ('id', 'to_account_number')
  search_fields = ('to_account_number',)
  list_per_page = 25

admin.site.register(Transfer, TransferAdmin)

class DepositAdmin(admin.ModelAdmin):
  list_display = ('id', 'to_account', 'amount', 'transaction_id')
  list_display_links = ('id', 'to_account')
  search_fields = ('to_account',)
  list_per_page = 25

admin.site.register(Deposit, DepositAdmin)

class WithdrawAdmin(admin.ModelAdmin):
  list_display = ('id', 'from_account', 'amount', 'transaction_id')
  list_display_links = ('id', 'from_account')
  search_fields = ('from_account',)
  list_per_page = 25

admin.site.register(Withdraw, WithdrawAdmin)

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'email', 'phone_number', 'query')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)