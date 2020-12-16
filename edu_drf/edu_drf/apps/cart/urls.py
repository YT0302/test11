from django.urls import path

from cart import views

urlpatterns=[
    # 自定义发送请求的类型 post->add_cart
    # path('add_cart/',views.CartViewSet.as_view({'post': 'add_cart', 'get': 'get_list_cart'}))
    path('options/',views.CartViewSet.as_view({'post': 'add_cart', 'get': 'get_list_cart'})),
    path('change/',views.CartItemViewSet.as_view({'post': 'create_set', 'delete': 'delete_set' })),
    path('cartcourse/',views.CartCourseViewSet.as_view({'delete': 'delete_course' })),
]