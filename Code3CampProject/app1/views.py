from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Author, Book, Publisher
from .forms import AuthorForm, BookForm, PublisherForm

# Author views
def author_list(request):
    authors = Author.objects.all()
    return render(request, 'app1/author_list.html', {'authors': authors})

def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'app1/author_form.html', {'form': form})

def author_update(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'app1/author_form.html', {'form': form})

def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == "POST":
        author.delete()
        return redirect('author_list')
    return render(request, 'app1/author_confirm_delete.html', {'author': author})



