from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import FeedBackForm, PoiskPeopl, Item_search, ProductForm


def index(request):
    return render(request, "page/index.html")


def reviev(request):
    return render(request, "page/reviev.html")


def product_form(request):
    if request.method == 'POST':
        fform = ProductForm(request.POST)
        if fform.is_valid():
            print('Очищенные данные из формы (POST):', fform.cleaned_data)
            print('Оценка (POST)', fform.cleaned_data['stars'])
    if request.method == 'GET':
        # fform = FeedBackForm()
        contextlib = {'form': ProductForm()}
        return render(request, 'page/product.html', context=contextlib)

def item_search(request):
    if request.method == 'POST':
        fform = Item_search(request.POST)
        if fform.is_valid():
            print('Очищенные данные из формы (POST):', fform.cleaned_data)
            print('Оценка (POST)', fform.cleaned_data['stars'])
    if request.method == 'GET':
        # fform = FeedBackForm()
        contextlib = {'form': Item_search()}
        return render(request, 'page/item_search.html', context=contextlib)


def poisk(request):
    if request.method == 'POST':
        fform = PoiskPeopl(request.POST)
        if fform.is_valid():
            print('Очищенные данные из формы (POST):', fform.cleaned_data)
            print('Оценка (POST)', fform.cleaned_data['stars'])
    if request.method == 'GET':
        # fform = FeedBackForm()
        contextlib = {'form': PoiskPeopl()}
        return render(request, 'page/people_poisk.html', context=contextlib)

def send(request):
    if request.method == 'POST':
        fform = FeedBackForm(request.POST)
        if fform.is_valid():
            print('Очищенные данные из формы (POST):', fform.cleaned_data)
            print('Оценка (POST)', fform.cleaned_data['stars'])
    if request.method == 'GET':
        # fform = FeedBackForm()
        contextlib = {'form': FeedBackForm()}
        print('Заголовок отзыва(GET):', request.GET.get('head'))
        print('Заголовок отзыва (GET):', request.GET.get('head'))
        return render(request, 'page/reviev.html', context=contextlib)
