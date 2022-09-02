from django.shortcuts import render


def http_status_404(request, exception, template_name='status/404.html'):
    return render(request, template_name, status=400)


def http_status_500(request, *args, **argv):
    return render(request, 'status/500.html', status=500)


def http_status_401(request):
    return render(request, 'status/401.html', status=401)
