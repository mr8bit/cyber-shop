from django.contrib import admin
from .models import *
# Register your models here.
class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    suit_classes = 'suit-tab suit-tab-images'


class CharacteristicInline(admin.TabularInline):
	model = Characteristic
	extra = 1
	suit_classes = 'suit-tab suit-tab-characteristic'

class ModificationInline(admin.TabularInline):
	model = Modification
	extra = 1
	suit_classes = 'suit-tab suit-tab-modification'


class ProductAdmin(admin.ModelAdmin):
	inlines = (ImageInline,ModificationInline,CharacteristicInline)
	fieldsets = [
        ('Основная информация', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
            	'title', 'slug','article', 'rating',
            	'gender', 'main_activity','status', 'price','last_price',
            	'category', 'brand', 'count'
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-images',),
            'fields': []}),
        (None, {
            'classes': ('suit-tab', 'suit-tab-modification',),
            'fields': []}),
        (None, {
            'classes': ('suit-tab', 'suit-tab-characteristic',),
            'fields': []}),
       	(None, {
            'classes': ('suit-tab', 'suit-tab-seo',),
            'fields': ['seo_description']}),
    ]
	suit_form_tabs = (('general', 'Основные'), 
		('images', 'Изображения'),
		('modification', 'Модификации'),
		('characteristic', 'Характеристики'),
		('seo', 'SEO'),

	)
     
admin.site.register(Modification)
admin.site.register(Brand)
admin.site.register(Product,ProductAdmin)
admin.site.register(Image)
admin.site.register(Category)
admin.site.register(Characteristic)
admin.site.register(CharacteristicType)
admin.site.register(ModificationType)