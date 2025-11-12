from django.db import models

# Create your models here.    
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    productName = models.CharField(max_length=100)
    quantityPerUnit = models.CharField(max_length=100)
    unitPrice = models.FloatField()
    discontinued = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.productName

class Shipper(models.Model):
    companyName = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.companyName

class Customer(models.Model):
    companyName = models.CharField(max_length=100)
    contactName = models.CharField(max_length=100)
    contactTitle = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)                  

    def __str__(self):
        return self.contactName

class Employee(models.Model):
    employeeName = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reportsTo = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.employeeName


class OrderDetails(models.Model):
    orderID = models.IntegerField()
    productID = models.IntegerField()
    unitPrice = models.FloatField()
    quantity = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    orderDate = models.DateField()
    requiredDate = models.DateField()
    shippedDate = models.DateField(null=True, blank=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    freight = models.FloatField()

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.contactName}"