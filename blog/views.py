from django.shortcuts import render, get_object_or_404
from .models import Small, Manfor, Womanfor, Bigges, Watch, Komputer, Koylak
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.
def computers(request):
    small = Small.objects.all()
    context = {
        'small': small
    }
    return render(request, 'computers.html', context=context)

def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponse("<h1>Siz eng zo'risiz </br> Raxmat </h1>")
    context = {
        'form': form
    }
    return render(request, 'contact.html', context=context)

def index(request):
    bigges = Bigges.objects.all()
    watch = Watch.objects.all()
    komputer = Komputer.objects.all()
    koylak = Koylak.objects.all()
    womanfor = Womanfor.objects.all()
    context = {
        'bigges': bigges,
        'watch': watch,
        'komputer': komputer,
        'koylak': koylak,
        'womanfor': womanfor
    }
    return render(request, 'index.html', context=context)

def mans_clothes(request):
    manfor = Manfor.objects.all()
    print("|Erkaklar uchun -->", manfor)
    context = {
        'manfor': manfor
    }
    return render(request, 'mans_clothes.html', context=context)
def womans_clothes(request):
    womanfor = Womanfor.objects.all()
    context = {
        'womanfor': womanfor
    }
    return render(request, 'womans_clothes.html', context=context)

def komputerDetail(request, komputer):
    kom = get_object_or_404(Komputer, slug=komputer)
    context = {
        'kom': kom
    }
    return render(request, 'komputerDetail.html', context=context)


def watchDetail(request, watch):
    wat = get_object_or_404(Watch, slug=watch)
    context = {
        'wat': wat
    }
    return render(request, 'watchDetail.html', context=context)

def koylakDetail(request, koylak):
    koy = get_object_or_404(Koylak, slug=koylak)
    context = {
        'koy': koy
    }
    return render(request, 'koylakDetail.html', context=context)

def womanforDetail(request, womanfor):
    woman = get_object_or_404(Womanfor, slug=womanfor)
    context = {
        'woman': woman
    }
    return render(request, 'womanforDetail.html', context=context)

def smallDetail(request, small):
    sma = get_object_or_404(Small, slug=small)
    context = {
        'sma': sma
    }
    return render(request, 'smallDetail.html', context=context)