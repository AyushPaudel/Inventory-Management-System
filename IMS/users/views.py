from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class testView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': "Congrats! you're in"}
        return Response(content)
