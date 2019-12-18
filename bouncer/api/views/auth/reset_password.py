from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import bcrypt
from ...models.user import User



class ResetPassword(APIView):

    def post(self, request):
        data = request.data

        password = data['password']
        token = data['token']

        if len(password) < 6:
            return Response({"message":"Invalid Password! Password must contain 6 or more characters"},
                    status=status.HTTP_400_BAD_REQUEST)
       
        result = User.objects.filter(forgot_password_token = token)
        
        if result.count() == 1:
            user = result[0]
            # hash user password using bcrypt algorithm
            hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            user.password = hashed
            user.save()
            message = "Your password has been sucessfully reset"
            return Response({"message":message},status=status.HTTP_200_OK)

        return Response(dict(error="This user does not exist"), status=status.HTTP_400_BAD_REQUEST)    
    