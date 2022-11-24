from django.db import models

# Create your models here.


class Orders(models.Model):
    orders_date_time = models.DateTimeField(auto_now=True)
    orders_name = models.CharField(max_length=200, verbose_name="Имя")
    orders_phone_num = models.CharField(max_length=15, verbose_name="Телефон")
    def __str__(self):
        return self.orders_name

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"