from rest_framework.pagination import PageNumberPagination

class CommentairePagination(PageNumberPagination):
    page_size = 10 