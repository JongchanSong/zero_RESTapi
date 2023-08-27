from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zero.models import Campus
from zero.serializer import CouponSerializer


# Create your views here.
@api_view(['GET'])
def get_coupons(request, campus_id):
    try:
        campus = Campus.objects.get(pk=campus_id)
    except Campus.DoesNotExist:
        return Response({"error": "Campus not found"}, status=404)


    coupon_data = get_coupons_data(campus)
    serializer = CouponSerializer

    return Response({"coupon_data": coupon_data})

"""get_coupons_data 함수를 구현 및 관련 데이터베이스 구축"""