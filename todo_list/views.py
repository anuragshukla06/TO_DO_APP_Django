from django.shortcuts import render
from .models import List
from .forms import ListForms
from django.contrib import messages

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = ListForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "The item has been added to the list!")
            all_items = List.objects.all
            render(request, 'homepage.html', {'allItems': all_items})

    all_items = List.objects.all
    return render(request, 'homepage.html', {'allItems' : all_items})
def about(request):
    return render(request, 'about.html', {})