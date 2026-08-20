from django.contrib import admin
from library.models import Author, Catagory,Publisher,Book

class  AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','created_at','updated_at')
    search_fields = ('name',)
    ordering = ('id',)
admin.site.register(Author, AuthorAdmin)

class  CatagoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','updated_at')
    search_fields = ('name',)
    ordering = ('id',)
admin.site.register(Catagory, CatagoryAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('id','name','created_at','updated_at')
    search_fields = ('name',)
    ordering = ('id',)
admin.site.register(Publisher, PublisherAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title','category','publisher','created_at','updated_at')
    search_fields = ('title','category','publisher')
    ordering = ('id',)
admin.site.register(Book, BookAdmin)


