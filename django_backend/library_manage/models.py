from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):

    """
    To Store Information About Authors
    """
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Publisher(models.Model):

    """
    To Store Information About Publishers
    """
    name = models.CharField(max_length=100)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):

    """
    To Store Information About Categories
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
 
    """
    To Store Information About Categories
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE) # Many to one Relationship
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=15, unique=True)
    publish_date = models.DateField()
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Member(models.Model):

    """
    To Store Information About Member of the Library
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    join_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class BorrowBooks(models.Model):

    """
    To Store Information About Borrowed book details
    """
    book = models.ForeignKey(Book, related_name='borrows', on_delete=models.CASCADE) # Many to one Relationship
    member = models.ForeignKey(Member, related_name='borrows', on_delete=models.CASCADE) # Many to one Relationship
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.book.title} borrowed by {self.member.first_name} {self.member.last_name}'

class Reservation(models.Model):

    """
    To Store Information About Users Who Wants To Reserve Books That Are Currently Unavailable.
    """
    user = models.ForeignKey(Member, related_name='reservations', on_delete=models.CASCADE) # Many to one Relationship
    book = models.ForeignKey(Book, related_name='reservations', on_delete=models.CASCADE) # Many to one Relationship
    reservation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reserved {self.book.title}"

class Penalty(models.Model):

    """
    To Store Information About Managing Penalties For Late Book Returns
    """
    user = models.ForeignKey(Member, related_name='penalties', on_delete=models.CASCADE) # Many to one Relationship
    borrowing = models.ForeignKey(BorrowBooks, related_name='penalties', on_delete=models.CASCADE) # Many to one Relationship
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"Penalty for {self.user.username}"

class Inventory(models.Model):

    """
    To Store Information About tracking the number of available copies of each book.
    """
    book = models.ForeignKey(Book, related_name='inventory', on_delete=models.CASCADE) # Many to one Relationship
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.book.title} - {self.quantity} available"

class Review(models.Model):

    """
    To store Information About User Reviews and Ratings for Books.
    """
    user = models.ForeignKey(Member, related_name='reviews', on_delete=models.CASCADE)  # Many to one relationship
    book = models.ForeignKey(Book, related_name='reviews', on_delete=models.CASCADE)  # Many to one relationship
    rating = models.PositiveIntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.book.title} by {self.user.username}"




