
from django.db import models



GENDER_CHOICES=[('M','Male'),
             ('f','Female'),
                ('o','others')]
ACCOUNT_TYPE=[('s','Savings account'),
              ('f','Fixed account'),
              ('sa','salary account'),
              ('c','current account'),
              ('n','NRI account'),
              ('r','reccuring deposit account')]


class Person(models.Model):
    name = models.CharField(max_length=100)
    Date=models.DateField()
    Age = models.IntegerField()
    Phone_number=models.CharField(max_length=12)
    Email = models.EmailField(max_length=300)
    Address = models.TextField()
    District = models.CharField(max_length=100)
    Branches = models.CharField(max_length=100)
    Gender= models.CharField(max_length=100,choices=GENDER_CHOICES)
    AccountType=models.CharField(max_length=100,choices=ACCOUNT_TYPE)

    def __str__(self):
        return '{}'.format(self.name)




class District(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)


class Branches(models.Model):
    name = models.CharField(max_length=100)
    District = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)





