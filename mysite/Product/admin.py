from django.contrib import admin
from . models import Product,CustomUser
from . models import Category,Staff,Customer,AdminCEO
from . models import Comment
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser,UserModel)




class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'is_published', 'created_at')
    list_display_links = ('id','name') 
    list_filter = ('price',)
    list_editable = ('is_published',)
    search_fields = ('name', 'price')
    ordering = ('price',)
    

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Staff)
admin.site.register(Customer)
admin.site.register(AdminCEO)

