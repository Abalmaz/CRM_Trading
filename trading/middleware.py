from django.utils.deprecation import MiddlewareMixin

from trading.models import Company


class SetCompanyMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'company_id' in request.session:
            session_company = request.session['company_id']
            company = Company.objects.get(pk=session_company)

            request.company = company

        response = self.get_response(request)

        return response
