from django.contrib import admin
from library.models import Catagory, Publisher, Book,Author,Authorbook,Booksdetail

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
    search_fields = ('title',)
    ordering = ('id',)
admin.site.register(Book, BookAdmin)

class  AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','created_at','updated_at')
    search_fields = ('id','name',)
    ordering = ('id',)
admin.site.register(Author,AuthorAdmin)

class  AuthorbookAdmin(admin.ModelAdmin):
    list_display = ('id','author','book','created_at','updated_at')
    search_fields = ('id',)
    ordering = ('id',)
admin.site.register(Authorbook,AuthorbookAdmin)

class BooksdetailAdmin(admin.ModelAdmin):
    list_display = ('id','isbn','pages','language','created_at','updated_at')
    search_fields = ('isbn',)
    ordering = ('id',)
admin.site.register(Booksdetail, BooksdetailAdmin)






