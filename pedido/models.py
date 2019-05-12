from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Order(models.Model):

    PREPARACION = 'En Preparación'
    LISTO = 'Listo para retirar'
    RETIRADO = 'Orden retirada'

    STATE_CHOICES = (
        (PREPARACION, 'En Preparación'),
        (LISTO, 'Listo para retirar'),
        (RETIRADO, 'Orden retirada'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_time = models.DateTimeField(default=timezone.now)
    date_pickup = models.DateTimeField(blank=True, null=True)
    detail = models.CharField(max_length=200)
    state = models.CharField(max_length=10, choices=STATE_CHOICES, default=PREPARACION)


    def publish(self):
        self.date_time = timezone.now()
        self.save()

    def __str__(self):
        return self.author

class Product(models.Model):
    photo = models.ImageField(blank=True, upload_to='product_img')
    description = models.CharField(max_length=200)
    price = models.CharField(max_length=6)

    def publish(self):
        self.save()

    def __str__(self):
        return self.description