from django.contrib.auth import get_user_model
from rest_framework import status, mixins, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from users.serializers import CreateUserSerializer, SelfInfoSerializer, SelfUpdateSerializer, UsersSerializer

User = get_user_model()


@api_view(['POST'])
def signup(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RetriveUpdateViewSet(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    pass


class SelfInfoViewSet(viewsets.ViewSet):
    @action(
        detail=False, methods=('get', 'patch'),
        url_path=r'me', permission_classes=(IsAuthenticated,)
    )
    def me(self, request, format=None):
        me = self.request.user
        if request.method == 'GET':
            serializer = SelfInfoSerializer(me)
            return Response(serializer.data)
        if request.method == 'PATCH':
            serializer = SelfUpdateSerializer(
                request.user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return_data = SelfInfoSerializer(me)
            return Response(data=return_data.data, status=status.HTTP_202_ACCEPTED)


class UsersViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser,)
