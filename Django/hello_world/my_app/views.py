from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
# Create your views here.

# def index(request):
#     return render(request, 'index.html')

def current_date(request):
    return HttpResponse(timezone.now())

def math_operation(request):
    result = 99 + 32 - 17 / 55
    return HttpResponse(f'Результат равен {result}')