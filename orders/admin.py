from django.contrib import admin
from .models import * 
class OrderItemInline(admin.TabularInline):
	model = OrderItem
	extra = 1
	suit_classes = 'suit-tab suit-tab-orderitem'

class OrderAdmin(admin.ModelAdmin):
	inlines = (OrderItemInline,)
	fieldsets = [
        ('Основная информация', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
            	'name'
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-orderitem',),
            'fields': []}),
    ]
	suit_form_tabs = (('general', 'Основные'), 
		('orderitem', 'Заказ'),

	)
admin.site.register(Order,OrderAdmin)

# Register your models here.
admin.site.register(OrderItem)
 