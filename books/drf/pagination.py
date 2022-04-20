from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    # Set any other options you want here like page_size
    page_size = 10
    page_size_query_param = "page_size"
    maz_page_size = 10

    def get_paginated_response(self, data):
        return Response(data)

    # def get_paginated_response(self, data):
    #     return Response(
    #         {
    #             "links": {
    #                 "next": self.get_next_link(),
    #                 "previous": self.get_previous_link(),
    #             },
    #             "count": self.page.paginator.count,
    #             "results": data,
    #         }
    #     )