from django.shortcuts import render

from django.shortcuts import render, redirect
from .forms import FeedBackForm


def index(request):
    return render(request, "page/index.html")


def reviev(request):
    return render(request, "page/reviev.html")


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

