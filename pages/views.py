from django.shortcuts import render


def home(request):
    return render(request, 'pages/index.html')


def archives(request):
    return render(request, 'pages/archives.html')


def demo(request):
    return render(request, 'pages/demo.html')


def page(request):
    return render(request, 'pages/page.html')


def blog(request):
    return render(request, 'pages/blog.html')


def single(request):
    return render(request, 'pages/single.html')