from bouncer.views import notfound
from django.urls import path, re_path


urlpatterns = [
    # register place other routes here ...

    # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
