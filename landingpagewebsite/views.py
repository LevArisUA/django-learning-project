from django.http import HttpResponse
from django.shortcuts import render


def first_page(request):
    a = "значение переменной а"
    b = "значение переменной b"
    return render(request, './index.html', {
        'a': a,
        "b": b
    })
