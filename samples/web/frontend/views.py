from django.views.static import serve
from django.conf import settings
import os


ROOT = settings.FRONTEND_PATH


def publish(request, path):
    if path.endswith('/') or path == '':
        path = path + 'index.html'
    if os.path.isfile(os.path.join(ROOT, path)):
        return serve(request, path, document_root=ROOT) 
    return serve(request, 'index.html', document_root=ROOT) 
