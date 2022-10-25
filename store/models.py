from django.db import models


class promotion(models.Model):
    description = models.CharField(max_length=225)
    discount = models.FloatField()


class product(models.Model):
    title = models.CharField(max_length=225)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    collection = models.ForeignKey('collection', on_delete=models.PROTECT)
    promotion = models.ManyToManyField(promotion)


class customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225)
    phone = models.IntegerField(max_length=11)
    birth_date = models.DateField(null=True)


class address(models.Model):
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    # OneToMany relationship .
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)


class collection(models.Model):
    title = models.CharField(max_length=225)


class order(models.Model):
    pass


class orderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.PROTECT)
    product = models.ForeignKey(order, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=None)
