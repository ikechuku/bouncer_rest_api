from django.urls import path, re_path
from bouncer.views import index, notfound


urlpatterns = [
    path('', index),

    # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
