from django.shortcuts import render
from .models import Orders
from .forms import OrdersForm


# Create your views here.
def first_page(request):
    object_list = Orders.objects.all()
    form = OrdersForm()
    return render(request, './index_old.html', {'object_list': object_list, 'form': form})


def thankyou(request):
    name = request.POST['name']
    phone = request.POST['phone']
    record = Orders(orders_name=name, orders_phone_num=phone)
    record.save()
    return render(request, './thankyou.html', {'name': name, 'phone': phone})