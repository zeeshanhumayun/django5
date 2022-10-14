from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1 style='text-align:center'>Hello, world. You're at the polls index of django website.</h1>")