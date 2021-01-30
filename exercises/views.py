from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .models import Exercise

def home_view(request, *args, **kwargs):    
    return render(request, 'pages/home.html', context = {}, status = 200)

def ex_list_view(request, *args, **kwargs):
    qs = Exercise.objects.all()
    ex_list = [{'id': x.id, 'content': x.content} for x in qs]
    data = {
        'is_user': False,
        'response': ex_list
    }
    return JsonResponse(data)

def ex_detail_view(request, *args, ex_id, **kwargs):
    data = {
        'id': ex_id,
    }
    status = 200
    try:
        obj = Exercise.objects.get(id=ex_id)
        data['content'] = obj.content
    except:
        data['message'] = 'not found'
        status = 404
    
    return JsonResponse(data, status = status)