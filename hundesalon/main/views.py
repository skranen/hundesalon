from django.http import HttpResponse
from django.shortcuts import render
from .models import Kunde, Bemerkungen, Bilder
import socket

def index(request):
    kunde = Kunde.objects.all()

    context = {
        'kunde':kunde,
    }

    return render(request, 'index.html',context)

def bemerkung(request,pk):
    kunde = Kunde.objects.get(pk=pk)

    if request.POST:
        text = request.POST.get('text', None)
        bemerkung = Bemerkungen.objects.create(
            text = text,
            kunde = kunde,
        )
        bemerkung.save()
    bemerkungen = Bemerkungen.objects.filter(kunde=kunde).order_by('-id')

    context = {
        'k':kunde,
        'bemerkungen':bemerkungen,
    }
    return  render(request, 'bemerkung.html', context)


def bilder(request, pk):
    kunde = Kunde.objects.get(pk=pk)
    bilder = Bilder.objects.filter(kunde=kunde)

    if request.method == 'POST' and request.FILES.get('bilder'):
        images = request.FILES.getlist('bilder')
        for image in images:
            Bilder.objects.create(kunde=kunde, bild=image)
        # Redirect or add success message here if needed.

    context = {
        'k': kunde,
        'images': bilder,
    }
    return render(request, 'images.html', context)