from django.http import JsonResponse

def home(request):
    message = 'You are not expected to be here, visit /api'
    return JsonResponse(dict(message=message), status=403)

def index(request):
    message = 'Welcome to Bouncer Rest API'
    return JsonResponse(dict(message=message))

def notfound(request):
    message = 'Route provided was not found'
    return JsonResponse(dict(message=message), status=404)
