from django.shortcuts import render_to_response, redirect, render
from .forms import ContactForm
from .models import Contact


def _form_view(request, template_name='basic.html', form_class=ContactForm):
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return render_to_response('thank.html', {'fa': f})
    else:
        form = form_class()
    return render(request, template_name, {'form': form})


def thank(request):
    return render(request, 'thank.html')


def index(request):
    return render(request, 'index.html')


def contact(request):
    return _form_view(request, template_name='contact.html')


def Rotract(request):
    return render(request, 'Rotract.html')


def d42(request):
    return render(request, 'd42.html')


def CSI(request):
    return render(request, 'CSI.html')


def NSS(request):
    return render(request, 'NSS.html')


def Aahvaan(request):
    return render(request, 'Aahvaan.html')


def Ecell(request):
    return render(request, 'Ecell.html')


def Parchhayi(request):
    return render(request, 'Parchhayi.html')


def IEEE(request):
    return render(request, 'IEEE.html')