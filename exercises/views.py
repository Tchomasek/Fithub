from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render

from .forms import SearchForm
from .models import Exercise, Tag

def home_view(request, *args, **kwargs):    
    return render(request, 'pages/home.html', context = {}, status = 200)

def search_view(request, *args, **kwargs):
    search = request.GET['search']
    print('---------------', search)
    return render(request, 'pages/search.html', context = {'search': search}, status = 200)

# def ex_search_list_view(request, *args, **kwargs):
#     search = request.POST['search']
#     #return render(request, 'pages/search.html', context={'search':search})
#     search_qs = Exercise.objects.filter(tags__name=search)
#     ex_search_list = [{'id': x.id, 'description': x.description, 'name': x.name, 'tags': x.tags.all()[0].name} for x in search_qs]
#     data = {
#         'search': ex_search_list
#     }
#     return JsonResponse(data)

def ex_list_view(request, *args, **kwargs):
    qs = Exercise.objects.all()
    ex_list = [{'id': x.id, 'description': x.description, 'name': x.name, 'tags': x.tags.all()[0].name} for x in qs]
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
        data['name'] = obj.name
        data['description'] = obj.description
    except:
        data['message'] = 'not found'
        status = 404
    
    return JsonResponse(data, status = status)