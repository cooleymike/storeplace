from django.db import models


class Promotion(models.Model):
    description = models.CharField(max_length=255)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=255)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')  # the + tells django not to create a reverse relationship

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    description = models.TextField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateTimeField(auto_now=True)
    # if accidentally delet collection you don't delete all products (PROTECT)
    # accidentally delete collection you don't delete all products as well
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer (models.Model):  # parent
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)  # could i have max_digits?
    birthdate = models.DateField(null=True)
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)


class Order(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'
    PAYMENT_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE, 'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING)
    # accidentally delete cust, you don't delete orders
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    # won't delete order items if you accidentally delete orders
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    # won't delete associated items if you accidentally delete product
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    # prevent negative values in this field
    quantity = models.PositiveSmallIntegerField()
    # always store price of product at order time
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):  # child
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)  # here you would have an extra value - PK set to True bc then you can only have one address to each customer.  (But I changed type of field to ForeignKey from OnetoOneField)
    # Cascade bc if I delete the customer associated address will also be deleted


class Cart(models.Model):
    # auto_now_add means field auto populated when you create a new cart
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    # Cascade delete cart, all items will also be deleted
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    # here product will be removed from all carts when it's deleted
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
