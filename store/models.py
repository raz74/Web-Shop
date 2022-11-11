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
    # promotion = models.ManyToManyField(promotion)


class customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'
    MEMBERSHIP_CHOICE = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=225)
    phone = models.CharField(max_length=11)
    birth_date = models.DateField(null=True)


class address(models.Model):
    street = models.CharField(max_length=225)
    city = models.CharField(max_length=225)
    # OneToMany relationship .
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)


class collection(models.Model):
    title = models.CharField(max_length=225)


class order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICE = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=1, choices=PAYMENT_STATUS_CHOICE, default=PAYMENT_STATUS_PENDING)


class orderItem(models.Model):
    order = models.ForeignKey(order, on_delete=models.PROTECT)
    product = models.ForeignKey(product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    # for saving change the price
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class cart(models.Model):
    creat_at = models.DateTimeField(auto_now_add=True)


class cartItem(models.Model):
    cart = models.ForeignKey(cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()