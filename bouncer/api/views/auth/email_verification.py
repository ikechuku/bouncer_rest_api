from rest_framework.permissions import IsAuthenticated
from django.http import Http404,JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from ...serializers.user_serializer import UserSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from ...models.user import User
class EmailVerificationView(APIView):
    #checks if user exists in database
    def check(self, *args):
        try:
            user = User.objects.get(email_verification_token=args[0])
            return user
        except:
            return False
    def get(self, request):
        return Response({"message": "Email verification endpoint"})
    """
    This function validates a user by collecting
    Token (string)
    Returns:
        Response (object) with
            - message
            - token
            - status
    """
    def post(self, request):
        token = request.data["email_verification_token"]
        user = self.check(token)
        if user and user.email_verified==False:
            refresh = RefreshToken.for_user(user)
            user.email_verified = True
            user.save()
            return Response({"message": "verified", "token": {
                'access':str(refresh.access_token)
            }, "verify_state":user.email_verified}, status=status.HTTP_202_ACCEPTED)
        elif user and user.email_verified==True:
            user.email_verified=False
            user.save()
            return Response({"message": "User already verified "}, status=status.HTTP_410_GONE)
        return Response({"message": "You've not registered with us"}, status=status.HTTP_404_NOT_FOUND)
