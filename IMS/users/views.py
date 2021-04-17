from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import MyTokenObtainPairSerializer, registerSerializer, \
                        changePasswordSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import imsUser
from rest_framework import generics
# Create your views here.


class testView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': "Congrats! you're in"}
        return Response(content)


class loginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class registerView(generics.CreateAPIView):
    queryset = imsUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = registerSerializer


class changePasswordView(generics.UpdateAPIView):

    queryset = imsUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = changePasswordSerializer



