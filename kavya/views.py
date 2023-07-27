from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kavya1 (request):
    return render(request,'kavya1.html')


def kavya2(request):
    return render(request,'kavya2.html')

def kavya3(request):
    return HttpResponse('am very good girl ammui')