from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


STATUS_CHOICES = (
    ('В наличии', 'В наличии'),
    ('Под заказ', 'Под заказ'),
    ('Отсутствует', 'Отсутствует'),
)
GENDER_CHOICES = (
    ('Мужское', 'Мужское'),
    ('Женское', 'Женское'),
 )
 
class Image(models.Model):
	url = models.ImageField(upload_to='uploads/')
	main_activity = models.BooleanField(default=False)
	product = models.ForeignKey('Product' , default='')
	def __str__(self):
		return str(self.url)

class ModificationType(models.Model):
	type = models.CharField(max_length=250,default='')
	def __str__(self):
		return str(self.type)

class Modification(models.Model):
	name = models.CharField( max_length = 250, default='')
	article = models.CharField(max_length=250, default='')
	count = models.PositiveIntegerField(default=1)
	type = models.ForeignKey('ModificationType', default='')
	product = models.ForeignKey('Product',default='')
	def __str__(self):
		return self.name

class Product(models.Model):
	time = models.DateTimeField(verbose_name= u'Дата публикации')
	title = models.CharField(max_length=100, verbose_name= u'Название')
	slug = models.SlugField(verbose_name= u'Url')
	rating = models.PositiveSmallIntegerField(default=0, verbose_name= u'Рэйтинг')
	article = models.CharField(max_length=250, verbose_name= u'Артикуль')
	gender = models.CharField(max_length=250,choices=GENDER_CHOICES, verbose_name= u'Пол')
	main_activity = models.BooleanField(verbose_name= u'Показать на главной')
	status = models.CharField(max_length=250,choices=STATUS_CHOICES, verbose_name= u'Статус')
	description = models.TextField(verbose_name= u'Описание')
	seo_description = models.TextField(verbose_name= u'SEO Описание', )
	count = models.PositiveIntegerField( verbose_name= u'Количество')
	price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name= u'Цена')
	last_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name= u'Предыдущая цена',default=0)
	category = models.ForeignKey('Category', verbose_name= u'Категория')
	brand = models.ForeignKey('Brand', verbose_name= u'Брэнд')
	def __str__(self):
		return self.title
	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

class Category(MPTTModel):
    name = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=250,choices=GENDER_CHOICES)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    slug = models.SlugField(editable=False)
    class MPTTMeta:
    	order_insertion_by=['name']
    def __str__(self):
    	return self.name

class Brand(models.Model):
	title = models.CharField(max_length=250,verbose_name= u'Название')
	description = models.TextField(verbose_name= u'Описание')
	image = models.ImageField()		
	def __str__(self):
		return self.title



class Characteristic(models.Model):
	name = models.CharField(max_length=240)
	product = models.ForeignKey('Product',default='')
	type = models.ForeignKey('CharacteristicType')
	def __str__(self):
		return self.name

class CharacteristicType(models.Model):
	type = models.CharField(max_length=230)	
	def __str__(self):
		return self.type