from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    exp_date = models.DateTimeField()
    exp_description = models.CharField(max_length=20)
    exp_amount =  models.BigIntegerField()
    exp_user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}__{}__{}".format(self.exp_date, self.exp_description, self.exp_amount)


class Income(models.Model):
    date = models.DateTimeField()
    description = models.CharField(max_length=20)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}__{}__{}".format(self.date, self.description, self.amount)
