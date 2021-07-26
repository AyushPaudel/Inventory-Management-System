from django.db.models import query
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import registerSerializer, changePasswordSerializer,\
                         updateProfileSerializer, logoutSerializer, adminTokenObtainPairSerializer,\
                         customTokenObtainPairSerializer, staffManagementSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import imsUser
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from .permissions import adminPermission
from ims_users.pagination import CustomPagination
# Create your views here.


class testView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': "Congrats! you're in"}
        return Response(content)


class loginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = customTokenObtainPairSerializer


class registerView(generics.CreateAPIView):
    queryset = imsUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = registerSerializer #only allow 'CU' in the user_type choice field.


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


# Admin login
class adminTokenObtainPairView(TokenObtainPairView):
    def is_user_admin(self, username):
        try:
            user = imsUser.objects.get(username=username)
            if user.user_type == 'AD':
                return True
            else: 
                return False

        except Exception as e:
            return False


    serializer_class = adminTokenObtainPairSerializer


    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        # get user 
        user = request.data['username']
        if self.is_user_admin(user):
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        else:
            return Response('{"not" : "done" }',status=status.HTTP_401_UNAUTHORIZED)


# Admin's staff management. 
class staffRegisterView(generics.CreateAPIView):
    queryset = imsUser.objects.filter(user_type="ST")
    permission_classes = (IsAuthenticated, adminPermission)
    serializer_class = registerSerializer #only allow 'ST' in the user_type choice field.


class staffProfileUpdate(generics.UpdateAPIView):
    queryset = imsUser.objects.filter(user_type="ST")
    permission_classes = (adminPermission,)
    serializer_class = updateProfileSerializer


class staffListView(generics.ListAPIView):
    queryset = imsUser.objects.filter(user_type="ST")
    permission_classes = (IsAuthenticated, adminPermission)
    serializer_class = staffManagementSerializer
    pagination_class = CustomPagination


class staffDetailView(generics.RetrieveAPIView):
    queryset = imsUser.objects.filter(user_type="ST")
    permission_classes = (IsAuthenticated, adminPermission)
    serializer_class = staffManagementSerializer
    
    