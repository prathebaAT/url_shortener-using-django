from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import URL
from .utils import generate_short_code

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['original_url']
        short_code = generate_short_code()
        url, created = URL.objects.get_or_create(original_url=original_url, defaults={'short_code': short_code})
        if not created:
            short_code = url.short_code
        return render(request, 'shortener/shorten_url.html', {'short_code': short_code})
    return render(request, 'shortener/shorten_url.html')

def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    return redirect(url.original_url)
