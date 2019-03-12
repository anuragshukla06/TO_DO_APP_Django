from django.shortcuts import render, redirect
from .models import List
from .forms import ListForms
from django.contrib import messages

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = ListForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "Item is added to list!")
            all_items = List.objects.all

    all_items = List.objects.all
    return render(request, 'homepage.html', {'allItems' : all_items})
def about(request):
    return render(request, 'about.html', {})

def delete(request, item_id):
    item = List.objects.get(pk = item_id)
    item.delete()
    return redirect('home')

def cross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = True
    item.save()
    return (redirect('home'))

def uncross(request, item_id):
    item = List.objects.get(pk=item_id)
    item.completed = False
    item.save()
    return (redirect('home'))

def edit(request, item_id):

    item = List.objects.all().get(pk = item_id)

    if request.method == 'POST':
        form = ListForms(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item is Edited!")
            all_items = List.objects.all
            return redirect('home')

    all_items = List.objects.all
    return render(request, 'edit.html', {'item' : item})