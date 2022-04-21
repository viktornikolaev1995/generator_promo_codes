from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, DestroyAPIView
from rest_framework.response import Response
from .models import Group, PromoCode
from .serializers import GroupListSerializer, GroupCreateSerializer, GroupPartialUpdateSerializer
from collections import OrderedDict


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


class GroupPartialUpdateAPIView(GenericAPIView):
    """Изменение количества и списка промо-кодов в группе"""
    serializer_class = GroupPartialUpdateSerializer

    @method_decorator(name='post', decorator=swagger_auto_schema(
        tags=['group'],
        operation_description="Здесь можно количество и список промо-кодов в группе",
        operation_id="group_partial_update",
        operation_summary="Изменение количества и списка промо-кодов в группе",
        responses={'201': 'Successful Response', '400': 'Bad Request', '401': 'Unauthorized', '403': 'Forbidden',
                   '422': 'Validation Error'}
    ))
    def post(self, request, *args, **kwargs):
        request_name = request.data.get('name')
        request_amount = request.data.get('amount')
        try:
            group = Group.objects.get(name=request_name)
        except ObjectDoesNotExist:
            return Response(data={'Group does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        promo_codes = PromoCode.objects.bulk_create([PromoCode(group=group) for _ in range(int(request_amount))])
        ret = OrderedDict()
        ret['name'] = group.name
        ret['promo_codes'] = [promo_code.key for promo_code in group.promo_codes.all()]
        group.amount += int(request_amount)
        group.save()
        return Response(data=ret, status=status.HTTP_201_CREATED)


class GroupDestroyAPIView(GenericAPIView):
    """Удаление групп с промо-кодами"""

    @method_decorator(name='delete', decorator=swagger_auto_schema(
        tags=['group'],
        operation_description="Здесь можно удалить группы с промо-кодами",
        operation_id="group_delete",
        operation_summary="Удаление групп с промо-кодами",
        responses={'204': 'Successful Response', '401': 'Unauthorized', '403': 'Forbidden'}
    ))
    def delete(self, request, *args, **kwargs):
        Group.objects.all().delete()
        return Response(data={'204': 'Successful Response'}, status=status.HTTP_204_NO_CONTENT)
