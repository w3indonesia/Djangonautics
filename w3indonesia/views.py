from django.shortcuts import render
from django.http import HttpResponse

# View untuk error 400
def custom_bad_request_view(request, exception=None):
    return render(request, 'errors/400.html', status=400)

# View untuk error 401
def custom_error_401(request, exception=None):
    return render(request, 'errors/401.html', status=401)

# View untuk error 403
def custom_permission_denied_view(request, exception=None):
    return render(request, 'errors/403.html', status=403)

# View untuk error 404
def custom_page_not_found_view(request, exception=None):
    return render(request, 'errors/404.html', status=404)

# View untuk error 405
def custom_method_not_allowed_view(request, exception=None):
    return render(request, 'errors/405.html', status=405)

# View untuk error 500
def custom_error_view(request, exception=None):
    return render(request, 'errors/500.html', status=500)

# View untuk error 502
def custom_bad_gateway_view(request, exception=None):
    return render(request, 'errors/502.html', status=502)

# View untuk error 503
def custom_service_unavailable_view(request, exception=None):
    return render(request, 'errors/503.html', status=503)
