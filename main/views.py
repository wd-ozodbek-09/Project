from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def service(request):
    return render(request, 'main/service.html')


def contact(request):
    return render(request, 'main/contact.html')


def read_more1(request):
    return render(request, 'main/read_more1.html')


def read_more2(request):
    return render(request, 'main/read_more2.html')


def read_more3(request):
    return render(request, 'main/read_more3.html')
