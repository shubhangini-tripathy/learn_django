from django.http import HttpResponse


def hello(request):
    text = "<h1>welcome to my app!</h1>"
    return HttpResponse(text)


def shubhi(request):
    text = "<h1>hello shubhi</h1>"
    return HttpResponse(text)
