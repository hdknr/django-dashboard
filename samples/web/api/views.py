from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    meta = dict((k, v) for (k, v) in request.META.items())
    ctx = {'name': 'index', 'meta': meta}
    return render(request, 'api/index.html',context=ctx)
