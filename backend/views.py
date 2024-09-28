from django.shortcuts import render
from app import models


def HOME(requests):
    explore = models.exploreproperties.objects.all()
    photo = models.ourcommunity.objects.all()

    data = {
        'explore':explore,
        "ourcommunity":photo,
    }

    return render(requests,'base.html',data)
