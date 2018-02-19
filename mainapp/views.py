from django.shortcuts import render_to_response, get_object_or_404, render
from mainapp.models import Book

def latest_book(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('index.html', {'book_list' : book_list})
    
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})