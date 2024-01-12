from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class CustomUser(AbstractUser):
    verified_member = models.BooleanField(default=False)
    email = models.EmailField(_('email address'), blank=False)
    pass
    def __str__(self):
        return self.username
    
class Picks(models.Model):
    NFL = "NFL"
    NHL = "NHL"
    NBA = "NBA"
    NCAAF = "NCAAF"
    NCAAM = "NCAAM"
    UFC = "UFC"
    WIN = "WIN"
    LOSS = "LOSS"
    NA = "NA"
    CATEGORY_CHOICES = {
        NFL: "NFL",
        NBA: "NBA",
        NCAAF: "NCAAF",
        NCAAM: "NCAAM",
        NHL: "NHL",
        UFC: "UFC",
    }
    OUTCOME_CHOICES = {
        WIN: "WIN",
        LOSS: "LOSS",
        NA: "NA"
    }
    pick_date = models.DateField('pickdate')
    pick_time = models.TimeField('picktime')
    category = models.CharField(
        max_length=5,
        choices=CATEGORY_CHOICES,
        default=NFL,
    )
    pick = models.CharField(max_length=200)
    units = models.IntegerField()
    outcome = models.CharField(
        max_length=4,
        choices=OUTCOME_CHOICES,
        default=NA,
    )
    closed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.pick)

    
