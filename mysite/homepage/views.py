from django.shortcuts import render
from .forms import ContactForm


def landing(request):
    return render(request, 'homepage/landing.html')

def index(request):
    return render(request, 'homepage/index.html')

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process the data in form.cleaned_data
            # For now, just redirect to the same page (you could also display a success message)
            return render(request, 'homepage/index.html', {'form': form, 'success': True})
    else:
        form = ContactForm()
    return render(request, 'homepage/index.html', {'form': form})
