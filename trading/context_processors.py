def company(request):
    if request.company:
        company = request.company
        return {'company': company}
