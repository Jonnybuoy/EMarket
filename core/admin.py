from django.contrib import admin
from .models import Item, OrderItem, Order, Payment, BillingAddress, Coupon


class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'ordered',
        'being_delivered',
        'received',
        'refund_requested',
        'refund_granted',
        'billing_address',
        'payment',
        'coupon']
    list_display_links = [
        'user',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = [ 'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted']

# Register your models here.
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(BillingAddress)
admin.site.register(Coupon)
