from django.shortcuts import render
from .models import Orders


# Create your views here.
def first_page(request):
    object_list = Orders.objects.all()
    return render(request, './index.html', {'object_list': object_list, 'b': '12345'})
