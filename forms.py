from django import forms
from .models import Transaction, Bill, Feedback
class TransactionForm(forms.ModelForm):
    class Meta:
        model=Transaction
        fields=["type","category","description","amount","date"]
        widgets={"date":forms.DateInput(attrs={"type":"date"})}
class BillForm(forms.ModelForm):
    class Meta:
        model=Bill
        fields=["category","description","amount","due_date","paid"]
        widgets={"due_date":forms.DateInput(attrs={"type":"date"})}
class FeedbackForm(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=["rating","comment"]
