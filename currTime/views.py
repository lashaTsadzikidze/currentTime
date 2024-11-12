from .models import DateTime
from .serializers import DateTimeSerializer
from django.http import JsonResponse
from datetime import datetime

# Create your views here.
def current_time(request):
    time_obj = DateTime.objects.create(datetime=datetime.now())

    serializer = DateTimeSerializer(time_obj)

    return JsonResponse(serializer.data)