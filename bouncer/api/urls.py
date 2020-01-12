
from bouncer.views import notfound
from django.urls import path, re_path, include
from .views.auth import login,email_verification,reset_password, forgot_password
from .views.customer import customer_view
from .views.vendor import vendor_view
from .views.product import get_product_details


urlpatterns = [
    # register other routes here ...
    path('auth/verify-email/',email_verification.EmailVerificationView.as_view(),name="email-verify" ),
    path('auth/forgot-password/',forgot_password.ForgotPassword.as_view(),name="forgot_password" ),
    path('customer/register/', customer_view.CustomerRegistration.as_view(), name='customer_register'),
    path('auth/login/', login.UserLogin.as_view(), name='login'),
    path('vendor/register/', vendor_view.VendorRegistration.as_view(), name='vendor_register'),
    path('auth/reset_password/', reset_password.ResetPassword.as_view(), name='reset_password'),
    path('product/', get_product_details.GetProductDetails.as_view(), name='get_product_details'),



    # match route that has not been registered above
    re_path(r'^(?:.*)$', notfound)
]
