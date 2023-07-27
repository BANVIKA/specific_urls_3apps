from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def kamakshi1 (request):
    return render(request,'kamakshi1.html')


def kamakshi2(request):
    return render(request,'kamakshi2.html')

def kamakshi3(request):
    return HttpResponse('am very good girl kamakshi')