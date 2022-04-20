from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import ListCreateAPIView
from .models import Group
from .serializers import GroupListSerializer, GroupCreateSerializer


class GroupListCreateAPIView(ListCreateAPIView):
    """Получение списка групп с промо-кодами или создание группы и промо-кодов к ней"""
    queryset = Group.objects.all().order_by('id')

    @method_decorator(name='get', decorator=swagger_auto_schema(
        tags=['group'],
        operation_description="Постраничное получение данных обо всех группах с промо-кодами",
        operation_id="group_list",
        operation_summary="Постраничное получение данных обо всех группах с промо-кодами",
        responses={'200': 'Successful Response', '400': 'Bad Request', '401': 'Unauthorized', '403': 'Forbidden',
                   '404': 'Not Found', '422': 'Validation Error'}
    ))
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_decorator(name='post', decorator=swagger_auto_schema(
        tags=['group'],
        operation_description="Здесь можно создать группу и промо-коды к ней",
        operation_id="group_create",
        operation_summary="Создание группы и промо-кодов к ней",
        responses={'201': 'Successful Response', '400': 'Bad Request', '401': 'Unauthorized', '403': 'Forbidden',
                   '422': 'Validation Error'}
    ))
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            self.serializer_class = GroupListSerializer
        elif self.request.method == 'POST':
            self.serializer_class = GroupCreateSerializer
        return self.serializer_class
