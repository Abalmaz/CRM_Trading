def company(request):
    if hasattr(request, 'company'):
        company = request.company
    else:
        company = None
    return {'company': company}

