from bouncer.views import home
from django.urls import path, re_path, include

urlpatterns = [
    # match all api prefixed url requests
    path('api/', include('api.urls')),

    # match all other routes and respond with 403
    re_path(r'^(?:.*)$', home)
]
