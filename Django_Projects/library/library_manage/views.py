
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .models import Author, Category, Publisher, Book, Member, BorrowBooks, Penalty, Review
from .serializers import AuthorSerializer, CategorySerializer, PublisherSerializer, BookSerializer, MemberSerializer, BorrowBooksSerializer, PenaltySerializer, ReviewSerializer

# Create your views here.

class AuthorView(APIView):

    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Author Added Successfully",safe=False)
        return JsonResponse("Failed to Add Author", safe=False)

    def get_author(self, pk):
        try:
            author = Author.objects.get(id=pk)
            return author
        except Author.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_author(pk)
            serializer = AuthorSerializer(data)
        else:
            data = Author.objects.all()
            serializer = AuthorSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Author Created Successfully", safe=False)
        return JsonResponse("Failed to Add Author", safe=False)

    def put(self, request, pk=None):
        author_to_update = Author.objects.get(id=pk)
        serializer = AuthorSerializer(instance=author_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Author Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Author")

    def delete(self, request, pk=None):
        author_to_delete = Author.objects.get(id=pk)
        author_to_delete.delete()
        return JsonResponse("Author Deleted Successfully", safe=False)

class CategoryView(APIView):

    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Category Added Successfully",safe=False)
        return JsonResponse("Failed to Category Author", safe=False)

    def get_category(self, pk):
        try:
            category = Category.objects.get(id=pk)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_author(pk)
            serializer = CategorySerializer(data)
        else:
            data = Category.objects.all()
            serializer = CategorySerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Category Created Successfully", safe=False)
        return JsonResponse("Failed to Add Category", safe=False)

    def put(self, request, pk=None):
        category_to_update = Category.objects.get(id=pk)
        serializer = CategorySerializer(instance=category_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Category Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Category")

    def delete(self, request, pk=None):
        category_to_delete = Category.objects.get(id=pk)
        category_to_delete.delete()
        return JsonResponse("Category Deleted Successfully", safe=False)

class PublisherView(APIView):

    def post(self, request):
        data = request.data
        serializer = PublisherSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Publisher Added Successfully",safe=False)
        return JsonResponse("Failed to Publisher Author", safe=False)

    def get_publisher(self, pk):
        try:
            publisher = Publisher.objects.get(id=pk)
            return publisher
        except Publisher.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_publisher(pk)
            serializer = PublisherSerializer(data)
        else:
            data = Publisher.objects.all()
            serializer = PublisherSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PublisherSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Publisher Created Successfully", safe=False)
        return JsonResponse("Failed to Add Publisher", safe=False)

    def put(self, request, pk=None):
        publisher_to_update = Publisher.objects.get(id=pk)
        serializer = PublisherSerializer(instance=publisher_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Publisher Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Publisher")

    def delete(self, request, pk=None):
        publisher_to_delete = Publisher.objects.get(id=pk)
        publisher_to_delete.delete()
        return JsonResponse("Publisher Deleted Successfully", safe=False)

class BookView(APIView):

    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Book Added Successfully",safe=False)
        return JsonResponse("Failed to Add Book", safe=False)

    def get_book(self, pk):
        try:
            book = Book.objects.get(id=pk)
            return book
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_book(pk)
            serializer = BookSerializer(data)
        else:
            data = Book.objects.all()
            serializer = BookSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Book Created Successfully", safe=False)
        return JsonResponse("Failed to Add Book", safe=False)

    def put(self, request, pk=None):
        book_to_update = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Book Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Book")

    def delete(self, request, pk=None):
        book_to_delete = Book.objects.get(id=pk)
        book_to_delete.delete()
        return JsonResponse("Book Deleted Successfully", safe=False)
    
class MemberView(APIView):

    def post(self, request):
        data = request.data
        serializer = MemberSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Member Added Successfully",safe=False)
        return JsonResponse("Failed to Member Book", safe=False)

    def get_member(self, pk):
        try:
            member = Member.objects.get(id=pk)
            return member
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_member(pk)
            serializer = MemberSerializer(data)
        else:
            data = Member.objects.all()
            serializer = MemberSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = MemberSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Member Created Successfully", safe=False)
        return JsonResponse("Failed to Add Member", safe=False)

    def put(self, request, pk=None):
        member_to_update = Member.objects.get(id=pk)
        serializer = MemberSerializer(instance=member_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Member Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Member")

    def delete(self, request, pk=None):
        member_to_delete = Member.objects.get(id=pk)
        member_to_delete.delete()
        return JsonResponse("Member Deleted Successfully", safe=False)

class BorrowBooksView(APIView):

    def post(self, request):
        data = request.data
        serializer = BorrowBooksSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Member Added Successfully",safe=False)
        return JsonResponse("Failed to Member Book", safe=False)

    def get_BorrowBooks(self, pk):
        try:
            borrow = BorrowBooks.objects.get(id=pk)
            return borrow
        except BorrowBooks.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_BorrowBooks(pk)
            serializer = BorrowBooksSerializer(data)
        else:
            data = BorrowBooks.objects.all()
            serializer = BorrowBooksSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = BorrowBooksSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Borrow Books Created Successfully", safe=False)
        return JsonResponse("Failed to Add Borrow Books", safe=False)

    def put(self, request, pk=None):
        borrow_to_update = BorrowBooks.objects.get(id=pk)
        serializer = BorrowBooksSerializer(instance=borrow_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Borrow Book Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Borrow Book")

    def delete(self, request, pk=None):
        borrow_to_delete = BorrowBooks.objects.get(id=pk)
        borrow_to_delete.delete()
        return JsonResponse("Borrow Book Deleted Successfully", safe=False)

class PenaltyView(APIView):

    def post(self, request):
        data = request.data
        serializer = PenaltySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Penalty Added Successfully",safe=False)
        return JsonResponse("Failed to Add Penalty", safe=False)

    def get_Penalty(self, pk):
        try:
            penalty = Penalty.objects.get(id=pk)
            return penalty
        except Penalty.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_Penalty(pk)
            serializer = PenaltySerializer(data)
        else:
            data = Penalty.objects.all()
            serializer = PenaltySerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = PenaltySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Penalty Created Successfully", safe=False)
        return JsonResponse("Failed to Add Penalty", safe=False)

    def put(self, request, pk=None):
        penalty_to_update = Penalty.objects.get(id=pk)
        serializer = PenaltySerializer(instance=penalty_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Penalty Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Penalty")

    def delete(self, request, pk=None):
        penalty_to_delete = Penalty.objects.get(id=pk)
        penalty_to_delete.delete()
        return JsonResponse("Penalty Deleted Successfully", safe=False)

class ReviewView(APIView):

    def post(self, request):
        data = request.data
        serializer = ReviewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Review Added Successfully",safe=False)
        return JsonResponse("Failed to Add Review", safe=False)

    def get_Penalty(self, pk):
        try:
            review = Review.objects.get(id=pk)
            return review
        except Review.DoesNotExist:
            raise Http404

    def get(self, request, pk=None):
        if pk:
            data = self.get_Penalty(pk)
            serializer = ReviewSerializer(data)
        else:
            data = Review.objects.all()
            serializer = ReviewSerializer(data, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = ReviewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Review Created Successfully", safe=False)
        return JsonResponse("Failed to Add Review", safe=False)

    def put(self, request, pk=None):
        review_to_update = Review.objects.get(id=pk)
        serializer =  ReviewSerializer(instance=review_to_update, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Review Updated Successfully", safe=False)
        return JsonResponse("Failed to Update Review")

    def delete(self, request, pk=None):
        Review_to_delete =  Review.objects.get(id=pk)
        Review_to_delete.delete()
        return JsonResponse("Review Deleted Successfully", safe=False)









