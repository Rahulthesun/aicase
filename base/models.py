from django.db import models

# Create your models here.
phone_choices = [
    ( 'i11', 'iphone11'),
    ( 'i12','iphone12' ),
    ( 'i13', 'iphone13'),
    ( 'i14', 'iphone14')

]

class Phone(models.Model):
    phone=models.CharField(max_length=200, blank=False,null=False, choices=phone_choices)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.phone