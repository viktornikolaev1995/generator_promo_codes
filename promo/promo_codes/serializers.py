from rest_framework import serializers
from .models import Group, PromoCode


class PromoCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromoCode
        fields = ['key']


class GroupCreateSerializer(serializers.ModelSerializer):
    """Group Create Serializer"""
    promo_codes = serializers.SlugRelatedField(slug_field='key', required=False, many=True, read_only=True)

    def create(self, validated_data):
        group = Group.objects.create(**validated_data)
        promo_codes = PromoCode.objects.bulk_create([PromoCode(group=group) for _ in range(group.amount)])
        return group

    def to_representation(self, instance):
        ret = super(GroupCreateSerializer, self).to_representation(instance)
        ret.pop('amount')
        return ret

    class Meta:
        model = Group
        fields = ['name', 'amount', 'promo_codes']


class GroupListSerializer(serializers.ModelSerializer):
    """Group List Serializer"""
    promo_codes = serializers.SlugRelatedField(slug_field='key', many=True, read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name', 'amount', 'promo_codes']


class GroupPartialUpdateSerializer(GroupCreateSerializer):
    """Group Partial Update Serializer"""
    pass
