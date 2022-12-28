from django.contrib import admin
from . models import Category,BlogPost,Comment

# class BlogAdmin(admin.ModelAdmin):
#     search_fields = ['heading','slug','body']
#     list_display = ['heading','category','slug','created']
#     list_filter = ['category','created']
#     prepopulated_fields = {'slug':('heading',)}


# class catAdmin(admin.ModelAdmin):
#     search_fields = ['name']
#     list_display = ['name','slug']
    
#     prepopulated_fields = {'slug':('name',)}

# class contAdmin(admin.ModelAdmin):
#     list_display = ['name','email','subject',]



admin.site.register(Category)
admin.site.register(BlogPost)
admin.site.register(Comment)
