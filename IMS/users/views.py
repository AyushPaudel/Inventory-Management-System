from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import registerSerializer, \
                        changePasswordSerializer, updateProfileSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import imsUser
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


class testView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': "Congrats! you're in"}
        return Response(content)

"""
class loginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer
"""

class registerView(generics.CreateAPIView):
    queryset = imsUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = registerSerializer


class changePasswordView(generics.UpdateAPIView):

    queryset = imsUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = changePasswordSerializer


class updateProfileView(generics.UpdateAPIView):

    queryset = imsUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = updateProfileSerializer


class logoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            

class logoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)