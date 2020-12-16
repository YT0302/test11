from rest_framework import status
from rest_framework.views import exception_handler
from rest_framework.response import Response

#全局异常处理
def custom_exception(exc,context):
    response =exception_handler(exc,context)
    print(66,exc,context)
    if response is None:
        return Response({
            'detail': '{} {}'.format(context['view'], exc)
        },status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response