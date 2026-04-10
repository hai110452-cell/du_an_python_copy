from django.contrib import admin
from .models import Category, Rock, Edm, Ballad,  Viet, Hiprap
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date']
    list_filter = ['date']
    search_fields = ['title']
    ordering = ['-date']  
admin.site.register(Category, CategoryAdmin)
admin.site.register(Rock, CategoryAdmin)
admin.site.register(Edm, CategoryAdmin)

admin.site.register(Ballad, CategoryAdmin)

admin.site.register(Hiprap, CategoryAdmin)
admin.site.register(Viet, CategoryAdmin)

