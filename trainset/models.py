from django.db import models


# Create your models here.
class Train(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    address = models.CharField(max_length=17)
    uuid = models.CharField(max_length=50)


class TrainStatus(models.Model):
    class TrainStatus(models.TextChoices):
        POWERED = 'POWERED', 'Powered'
        RUNNING = 'RUNNING', 'Running'
        OFF = 'OFF', 'Off'
    train = models.ForeignKey(Train)
    status = models.CharField(max_length=20)
