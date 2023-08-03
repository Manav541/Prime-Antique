from django.db import models

from django.db import models

# Create your models here.

class user(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=35)
    address = models.CharField(max_length=300)
    contact = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    dob = models.DateField()
    role_id = models.IntegerField()
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(null=True)

    class Meta:
        db_table ="user"

class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=20)
    subcategory_id = models.OneToOneField("self", null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "category"

class product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey(category, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_image = models.ImageField(max_length=200)
    product_desc = models.CharField(max_length=300)

    class Meta:
        db_table = "product"

class product_details(models.Model):
    product_details_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    product_details_price = models.CharField(max_length=20)
    product_details_qty = models.IntegerField(null=False)

    class Meta:
        db_table = "product_details"


class cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    cart_date = models.DateField()
    cart_qty = models.IntegerField()
    total_amt = models.IntegerField()

    class Meta:
        db_table = "cart"


class order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13)
    address = models.CharField(max_length=300)
    order_date = models.DateField(null=False)
    order_status = models.CharField(max_length=20)
    total_amount = models.IntegerField(null=False)
    order_certificate = models.ImageField(max_length=200)
    payment_status = models.CharField(max_length=20)

    class Meta:
        db_table = "order"

class order_item(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    order_item_date = models.DateField(null=False)
    order_item_address = models.CharField(max_length=300)
    order_item_qty = models.IntegerField(null=False)

    class Meta:
        db_table = "orderitem"

class payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey(order, on_delete=models.CASCADE)
    payment_amount = models.IntegerField(null=False)
    payment_status = models.CharField(max_length=20)
    payment_date = models.DateField(null=False)

    class Meta:
        db_table = "payment"

class feedback(models.Model):
    feedback_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    product_id = models.ForeignKey(product, on_delete=models.CASCADE)
    feedback_date = models.DateField(null=False)
    feedback_desc = models.CharField(max_length=200)

    class Meta:
        db_table = "feedback"