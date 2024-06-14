from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
from celery.result import AsyncResult

# Create your views here.

def test(request):
    task = test_func.delay()
    print(task)
    return HttpResponse("Done")

def status(request,pk):
    task = AsyncResult(pk)
    print(task.state)
    response = {
        'state': task.state,
        'current': 0,
        'total': 1,
    }
    if task.state == 'PENDING':
        response['state'] = task.state
        response['current'] = 0
        response['total'] = 100
    elif task.state == 'PROGRESS':
        response.update(task.info)
    elif task.state == 'SUCCESS':
        response.update(task.result)
    elif task.state == 'FAILURE':
        response['state'] = task.state
        response['current'] = 0
        response['total'] = 1
        response['status'] = str(task.info)
    return HttpResponse(response)