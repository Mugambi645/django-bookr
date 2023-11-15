from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    name = "world"
    return render(request, "base.html", {"name": name})