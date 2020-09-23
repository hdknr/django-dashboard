from django.middleware.csrf import get_token
import traceback
from logging import getLogger

logger = getLogger(__name__)


class CorsMiddleware(object):

    def process_response(self, request, response):
        response['X-CSRFToken'] = get_token(request)
        response['X-IsAuthenticated'] = request.user.is_authenticated
        return response
    
    def process_request(self, request):
        pass

    def __init__(self, get_response):
        # https://docs.djangoproject.com/en/3.0/topics/http/middleware/
        self.get_response = get_response

    def __call__(self, request):
        try:
            self.process_request(request)
        except:
            logger.error(traceback.format_exc())

        response = self.get_response(request)
        return self.process_response(request, response)

