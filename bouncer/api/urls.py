
import sys
sys.path.append('..')
from bouncer.views import notfound
from django.urls import path, re_path, include
from .views.user import customers, login
from .views.user.email_verification import EmailVerify,show

urlpatterns = [
    # register other routes here ...
    path('auth/verify-email/',EmailVerify.as_view(),name="email-verify" ),
    path('show/',show,name="show" ),
    path('customer/register/', customers.CustomerRegistration.as_view(), name='customer_register'),
    path('auth/login/', login.UserLogin.as_view(), name='login'),

    # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
