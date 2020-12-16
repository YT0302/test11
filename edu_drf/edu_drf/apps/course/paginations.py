from rest_framework.pagination import PageNumberPagination


class coursePageNumberPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'size'
    page_size = 3
    max_page_size = 10