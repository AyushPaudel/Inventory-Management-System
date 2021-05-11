from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import registerSerializer, changePasswordSerializer,\
                         updateProfileSerializer, logoutSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import imsUser
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
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
    serializer_class = logoutSerializer

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

class logoutAllView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        tokens = OutstandingToken.objects.filter(user_id=request.user.id)
        for token in tokens:
            t, _ = BlacklistedToken.objects.get_or_create(token=token)

        return Response(status=status.HTTP_205_RESET_CONTENT)
