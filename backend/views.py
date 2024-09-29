from django.shortcuts import render
from app import models


def HOME(requests):
    properties = models.exploreproperties.objects.all()
    photo = models.ourcommunity.objects.all()
    media = models.media.objects.all()

    data = {
        'properties':properties,
        "ourcommunity":photo,
        "media":media,
    }

    return render(requests,'base.html',data)
