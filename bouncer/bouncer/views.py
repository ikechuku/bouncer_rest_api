from django.http import JsonResponse
from django.core.mail import send_mail

def home(request):
    message = 'You are not expected to be here, visit /api'
    return JsonResponse(dict(message=message), status=403)

def index(request):
    send_mail(
        "Nice Subject",
        'Nice Body',
        'abdulfataiaka@gmail.com',
        ['abdulfataia@decagonhq.com'],
        fail_silently=False,
        # html_message='<a href="localhost:8100/email_verify/ab">link</a>'
    )
    message = 'Welcome to Bouncer Rest API'
    return JsonResponse(dict(message=message))

def notfound(request):
    message = 'Route provided was not found'
    return JsonResponse(dict(message=message), status=404)
