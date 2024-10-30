from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def home(request):
    template = loader.get_template('home.html')
    context = {
        'about_us': 'This is a website about us.',
        'services': [
            {
                'title': 'Service 1',
                'thumbnail': '/static/images/service1.png',
            },
            {
                'title': 'Service 2',
                'thumbnail': '/static/images/service2.png',
            },
            {
                'title': 'Service 3',
                'thumbnail': '/static/images/service3.png',
            },
        ],
        'contact_form': {
            'name': '',
            'email': '',
            'message': '',
        },
    }
    return HttpResponse(template.render(context, request))
