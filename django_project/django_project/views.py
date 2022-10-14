from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='text-align:center'>Zeeshan Hello, world. You're at the polls index of django website.</h1>")