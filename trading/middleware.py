from datetime import datetime

from django.utils.deprecation import MiddlewareMixin


class SetCompanyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.user.username = 'Middleware'
        request.middleware_company = "My Company"
        return

    # def __init__(self, get_response):
    #     self.get_response = get_response
    #
    # def __call__(self, request):
    #
    #     if request.user.is_authenticated:
    #
    #         request.time = datetime.now()
    #         request.user.username = 'middleware'
    #
    #     response = self.get_response(request)
    #
    #     return response
