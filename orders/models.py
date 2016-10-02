from django.db import models



class Order(models.Model):
	name = models.CharField(max_length=300)
	amount = models.PositiveIntegerField(verbose_name= u'Сумма заказа',default='')
 
class OrderItem(models.Model):
	product = models.ForeignKey('catalog.Product')
	quantity = models.PositiveIntegerField()
	order = models.ForeignKey('Order')


class Adress(models.Model):
	country = models.CharField(max_length=300)
	street = models.CharField(max_length=300)
	index = models.CharField(max_length=300)
	product = models.ForeignKey('catalog.Product')

