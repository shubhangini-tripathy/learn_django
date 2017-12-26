# from django.http import HttpResponse


# def hello(request):
#     text = "<h1>welcome to my app!</h1>"
#     return HttpResponse(text)


# def shubhi(request):
#     text = "<h1>hello shubhi</h1>"
#     return HttpResponse(text)

# def ashu(request):
#     text = "<h1>hello shubhi</h1>"
#     return HttpResponse(text)

from django.views.generic import TemplateView


class ShubhiPageView(TemplateView):
    template_name = 'shubhi.html'
class AshuPageView(TemplateView):
    template_name = 'ashu.html'

