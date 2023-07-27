from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kaveri1 (request):
    return render(request,'kaveri1.html')


def kaveri2(request):
    return render(request,'kaveri2.html')

def kaveri3(request):
    return HttpResponse('am very good girl kaveri')