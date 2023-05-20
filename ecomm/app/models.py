from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinLengthValidator
# Create your models here.
STATE_CHOICES = (
    ('Andaman & Nicobar Island','Andaman & Nicobar Island'),
    ('Andra Pradesh','Andra Pradesh'),
    ('Arunachal Pradesh','Arunachal Pradesh'),
    ('Assam','Assam'),
    ('Bihar','Bihar'),
    ('Chhattisgarh','Chhattisgarh'),
    ('Chandigarh','Chandigarh'),
    ('Dadra & Nagar Haveli','Dadra & Nagar Haveli'),
    ('Delhi','Delhi'),
    ('Madhya Pradesh','Madhya Pradesh'),
    ('Uttar Pradesh','Uttar Pradesh'),
    ('Maharastra','Maharastra'),
    ('Mizoram','Mizoram'),
    ('Nagaland','Nagaland')
)
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    state = models.CharField(choices = STATE_CHOICES,max_length=50)

    def __str__(self):
        return str(self.id)
    
CATEGORY_CHOICES = (
    ('E' , 'Electronics'),
    ('A' , 'Accessories'),
    ('TW' , 'Top Wear'),
    ('BW' , 'Bottom Wear')
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices  = CATEGORY_CHOICES,max_length=2)
    product_image = models.ImageField(upload_to ='producting' )
    
    def __str__(self):
        return str(self.id)
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
STAUS_CHOICES = (
    ('Accepted','Accepted'),
    ('packed' , 'packed'),
    ('On The Key','On The Way'),
    ('Cancle' , 'Cancle')
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models .ForeignKey(Customer,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices = STAUS_CHOICES,default='Pending')
    

