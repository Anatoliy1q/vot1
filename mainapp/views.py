from django.shortcuts import render_to_response,redirect,render, get_object_or_404
from mainapp.models import Book
from django.http import HttpResponse
from .forms import BookForm
from django.utils import timezone

def search_form(request):
    return render_to_response('search_form.html')
    

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(name__contains=q)
        return render(request, 'search_results.html', {'books': books, 'query': q})
    else:
        return HttpResponse("Please submit a search form")


def latest_book(request):
    book_list = Book.objects.order_by('-pub_date')[:10]
    return render_to_response('index.html', {'book_list' : book_list})
 

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'book_detail.html', {'book': book})
    
def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.pub_date = timezone.now()
            book.save()
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form': form})

        
