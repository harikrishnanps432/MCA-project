from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TYPE_CHOICES=[("income","Income"),("expense","Expense")]
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    type=models.CharField(max_length=10,choices=TYPE_CHOICES)
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=255,blank=True)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    date=models.DateField()
    def __str__(self): return f"{self.type}: {self.amount}"

class Bill(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=255,blank=True)
    amount=models.DecimalField(max_digits=12,decimal_places=2)
    due_date=models.DateField()
    paid=models.BooleanField(default=False)
    def __str__(self): return self.category

class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    rating=models.PositiveSmallIntegerField()
    comment=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
