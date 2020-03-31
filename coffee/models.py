from django.db import models


class Products(models.Model):

    product_name = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=20, default="")
    subcatogory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="coffee/images/", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=20, default="")
    phone = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, default="")

    def __str__(self):
        return self.name
class Orders(models.Model):
    order_id=models.AutoField(primary_key=True)
    item_json=models.CharField(max_length=2000)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    address1=models.CharField(max_length=150)
    address2=models.CharField(max_length=150,default=" ")
    state=models.CharField(max_length=80)
    city=models.CharField(max_length=50)
    zip_code=models.CharField(max_length=10)
    amount=models.IntegerField(default=0)
    phone=models.IntegerField()
class Order_update(models.Model):
    update_id=models.AutoField(primary_key=True)
    orderId=models.IntegerField(default="")
    update_desc=models.CharField(max_length=2000)
    timestamp=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.update_desc[0:7]+"...."