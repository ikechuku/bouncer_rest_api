import sys
sys.path.append("..")
from rest_framework.permissions import IsAuthenticated
from django.http import QueryDict, Http404,JsonResponse
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config
from rest_framework import status
from ...serializers.userSerializers import UserSerializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view,permission_classes
from ...models.user.users import User

class EmailVerify(APIView):
    def check(self, *args):
        try:
            user = User.objects.get(token=args[0])
            return user
        except:
            return False
    def get(self, request):
        return Response({"message": "Email verification endpoint"})
    def post(self, request):
        token = request.data["token"]
        user = self.check(token)
        if user and user.email_verified==False:
            refresh = RefreshToken.for_user(user)
            user.email_verified = True
            user.save()
            return Response({"message": "verified", "token": {
                'refresh':str(refresh),
                'access':str(refresh.access_token)
            }, "verify_state":user.email_verified}, status=status.HTTP_202_ACCEPTED)
        elif user and user.email_verified==True:
            user.email_verified=False
            user.save()
            return Response({"message": "User already verified "}, status=status.HTTP_410_GONE)
        return Response({"message": "You've not registered with us"}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def show(request):
    return JsonResponse(dict(message='Welcome ', ticket="12345"), status=200)