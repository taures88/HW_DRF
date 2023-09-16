from rest_framework.pagination import PageNumberPagination


class StudiesPaginator(PageNumberPagination):
    page_size = 6