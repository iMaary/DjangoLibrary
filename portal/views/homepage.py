from django.shortcuts import render
from portal.models import StaticText

def homepage(request):
    context = {
        'homepage_title': get_static_text('homepage_title'),
        'homepage_intro': get_static_text('homepage_intro'),
        'footer_note': get_static_text('footer_note'),
    }
    return render(request, 'index.html', context)

def get_static_text(key):
    try:
        return StaticText.objects.get(key=key).content
    except StaticText.DoesNotExist:
        return f'{{ texto não encontrado: {key} }}'
