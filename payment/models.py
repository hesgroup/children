from django.db import models


class Transaction(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    amount = models.IntegerField()
    status = models.CharField(default='pending', max_length='200')
    start_date = models.DateTimeField(auto_now=True)


class TransactionResult(models.Model):
    transaction = models.ForeignKey(Transaction)
    status = models.CharField(max_length=100)
    refnumber = models.CharField(max_length=30)
    resnumber = models.IntegerField()
    verify_response = models.CharField(null=True, blank=True, max_length=500)
