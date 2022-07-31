from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import RegisterSerializer
# Create your views here.


class CreateNewUser(APIView):
    permission_classes = [AllowAny]
    """
    In the future I woudl add something like "users_company"
    where user provides a company uuid then admin of set company
    can authenticate user 
    """

    def post(self, request):
        reg_ser = RegisterSerializer(data=request.data)
        if reg_ser.is_valid():
            new_user = reg_ser.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(reg_ser.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistToken(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_200)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
