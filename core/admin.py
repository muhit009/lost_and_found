from django.contrib import admin
from .models import LostItem,FoundItem
# Register your models here.

# admin.site.register(LostItem)
# admin.site.register(FoundItem)
@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_lost', 'claimed')
    
@admin.register(FoundItem)
class FoundItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_found', 'claimed')