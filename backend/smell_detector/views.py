from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from .models import Smell

@require_POST
def detect_smells(request):
    data = json.loads(request.body)
    smells = Smell.objects.filter(category__in=data['categories'])
    return JsonResponse({'smells': list(smells.values())})
