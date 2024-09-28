from django.contrib import admin
from library_manage.models import Author, Publisher, Category, Book, Member, BorrowBooks, Penalty, Review

# Register your models here.

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(BorrowBooks)
admin.site.register(Penalty)
admin.site.register(Review)