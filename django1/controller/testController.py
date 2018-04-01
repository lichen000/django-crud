import logging
import traceback
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def test1(request):
    x = 1
    y = 0
    try:
        z = x / y
    except Exception as e:
        logger.error(traceback.format_exc())
    return HttpResponse("end")