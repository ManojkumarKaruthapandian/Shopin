from django.db import models
from django.contrib.auth.models import User
import datetime
import os

def getfilename(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class Catagory(models.Model):
    name=models.CharField(max_length=150,null=True,blank=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.CharField(max_length=150,null=False,blank=False)
    name=models.CharField(max_length=500,null=False,blank=False)
    product_image=models.ImageField(max_length=500,upload_to=getfilename,null=True,blank=True)
    description=models.TextField(max_length=5000,null=False,blank=False)
    quantity=models.IntegerField(null=False,blank=False)
    selling_price=models.FloatField(null=False,blank=False)
    original_price=models.FloatField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=False,help_text="0-show,1-Hidden")
    todays_deal=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_Mobiles=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_Fashion=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_Electronics=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_Sports=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_Appliances=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_ToysBeauty=models.BooleanField(default=False,help_text="0-default,1-trending")
    trending_Grocery=models.BooleanField(default=False,help_text="0-default,1-trending")
    
   

    def __str__(self):
        return self.name  


    
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)

    @property
    def total_cost(self):
        return self.product_qty*self.product.selling_price


class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=True,blank=True)
    create_at=models.DateTimeField(auto_now_add=True)



class Favorite(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)



class Recentview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    create_at=models.DateTimeField(auto_now_add=True)

   


