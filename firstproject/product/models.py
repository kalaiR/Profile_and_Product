from django.db import models

class Product_detail(models.Model):
	product_name=models.CharField(null=True,max_length=50)
	price=models.FloatField(null=True, max_length=50)
	product_model=models.CharField(null=True,max_length=50)
	product_description=models.CharField(null=True,max_length=50)
	# product_image=models.FileField(upload_to='post_product/static/img/product4.png')


