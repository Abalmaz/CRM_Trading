from django.utils.deprecation import MiddlewareMixin

from trading.models import Company


class SetCompanyMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if not request.user.is_anonymous:
            try:
                session_company = request.session['company_id'] if \
                    'company_id' in request.session else \
                    request.user.company.filter(is_default=True).\
                    first().company.pk
                request.session['company_id'] = session_company
            except:
                return self.get_response(request)
            company = Company.objects.get(pk=session_company)

            request.company = company

        response = self.get_response(request)

        return response
