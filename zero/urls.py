from django.urls import path

from . import views

urlpatterns = [
    # ... 다른 URL 패턴들 ...
    path('api/campuses/<int:campus_id>/map/', views.get_map, name='get-map'),
    path('api/campuses/<int:campus_id>/coupons/', views.get_coupons, name='get-coupons'),
]