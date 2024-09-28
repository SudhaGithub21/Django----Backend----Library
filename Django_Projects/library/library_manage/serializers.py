from rest_framework import serializers
from .models import Author, Publisher, Category, Book, Member, BorrowBooks, Penalty, Review

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'bio')
    #exclude option also here - Don want to serialize the particular field
    #exclue=['name']
    
class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name', 'address']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()
    categories = CategorySerializer(many=True)
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publisher', 'isbn', 'publish_date', 'categories']

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'first_name', 'last_name', 'email', 'phone', 'join_date']

class BorrowBooksSerializer(serializers.ModelSerializer):
    book = BookSerializer()
    member = MemberSerializer()

    class Meta:
        model = BorrowBooks
        fields = ['id', 'book', 'member', 'loan_date', 'return_date']

class PenaltySerializer(serializers.ModelSerializer):
    user = MemberSerializer()
    borrowing = BorrowBooksSerializer()

    class Meta:
        model = Penalty
        fields = ['id', 'user', 'borrowing', 'amount', 'paid']

class ReviewSerializer(serializers.ModelSerializer):
    user = MemberSerializer()
    book = BookSerializer()

    class Meta:
        model = Review
        fields = ['id', 'user', 'book', 'rating', 'comment', 'created_at']