from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    quantity_per_unit = models.CharField(max_length=100)
    unit_price = models.FloatField()
    discontinued = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name

class Shipper(models.Model):
    company_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name

class Customer(models.Model):
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=100)
    contact_title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_name

class Employee(models.Model):
    employee_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    reports_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.employee_name

class OrderDetails(models.Model):
    order_id = models.IntegerField()
    product_id = models.IntegerField()
    unit_price = models.FloatField()
    quantity = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return f"OrderDetails #{self.pk}"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.DateField(null=True, blank=True)
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE)
    freight = models.FloatField()

    def __str__(self):
        return f"Order #{self.pk} by {self.customer.contact_name}"
