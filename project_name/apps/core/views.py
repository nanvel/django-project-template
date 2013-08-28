from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseServerError, HttpResponseNotFound


def handler500(request, template_name='500.html'):
    t = get_template(template_name)
    ctx = Context({})
    return HttpResponseServerError(t.render(ctx))


def handler404(request, template_name='404.html'):
    t = get_template(template_name)
    ctx = Context({})
    return HttpResponseNotFound(t.render(ctx))
