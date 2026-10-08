from django.contrib import admin
from .models import Transaction, Bill, Feedback
admin.site.register(Transaction)
admin.site.register(Bill)
admin.site.register(Feedback)
