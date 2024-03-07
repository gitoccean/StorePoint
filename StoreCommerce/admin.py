from django.contrib import admin
from .models import (db_Product, db_Mobile, db_Computer, db_Shoes, db_Cloth, db_Watch, db_TV, db_Product_Image, db_Product_Order, db_Place_Order, db_Accessories, db_Wishlist, db_Review,db_Message_Admin,db_Comment)
# Register your models here.


admin.site.register(db_Product)
admin.site.register(db_Mobile)
admin.site.register(db_Computer)
admin.site.register(db_Shoes)
admin.site.register(db_Cloth)
admin.site.register(db_Watch)
admin.site.register(db_TV)
admin.site.register(db_Product_Image)
admin.site.register(db_Product_Order)
admin.site.register(db_Place_Order)
admin.site.register(db_Accessories)
admin.site.register(db_Wishlist)
admin.site.register(db_Review)
admin.site.register(db_Message_Admin)
admin.site.register(db_Comment)






'''
class Product_Inline(admin.TabularInline):
    model = db_Product 

class db_Product_Inline(admin.ModelAdmin):
    inlines = [Product_Inline]

admin.site.register(db_Mobile, db_Product_Inline)
'''