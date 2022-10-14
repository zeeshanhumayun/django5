from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, world. You're at the polls index of django website.</h1>")