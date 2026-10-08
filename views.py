from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Sum
from .models import Transaction, Bill, Feedback
from .forms import TransactionForm, BillForm, FeedbackForm

def home(request):
    if not request.user.is_authenticated:
        return render(request,"home.html")
    income=Transaction.objects.filter(user=request.user,type="income").aggregate(Sum("amount"))["amount__sum"] or 0
    expense=Transaction.objects.filter(user=request.user,type="expense").aggregate(Sum("amount"))["amount__sum"] or 0
    bills=Bill.objects.filter(user=request.user,paid=False).order_by("due_date")
    return render(request,"dashboard.html",{"income":income,"expense":expense,"balance":income-expense,"bills":bills})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(); login(request,user); return redirect("home")
    else: form=UserCreationForm()
    return render(request,"register.html",{"form":form})

@login_required
def add_transaction(request):
    form=TransactionForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False); obj.user=request.user; obj.save(); return redirect("home")
    return render(request,"form.html",{"form":form,"title":"Add Income / Expense"})

@login_required
def bills(request):
    if request.method=="POST":
        form=BillForm(request.POST)
        if form.is_valid():
            obj=form.save(commit=False); obj.user=request.user; obj.save(); return redirect("bills")
    else: form=BillForm()
    return render(request,"bills.html",{"form":form,"bills":Bill.objects.filter(user=request.user)})

@login_required
def feedback(request):
    form=FeedbackForm(request.POST or None)
    if form.is_valid():
        obj=form.save(commit=False); obj.user=request.user; obj.save(); return redirect("home")
    return render(request,"form.html",{"form":form,"title":"Feedback and Rating"})
