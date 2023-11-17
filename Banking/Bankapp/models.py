from django.db import models

# Create your models here.
class Customer(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    materials_provided = models.TextField()

    def __str__(self):
        return self.name





# class Branch(models.Model):
#     district = models.CharField(max_length=100)
#     sub_area = models.CharField(max_length=100)