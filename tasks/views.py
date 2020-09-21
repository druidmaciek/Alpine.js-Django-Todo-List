from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from tasks.models import Task


def index(request):
    return render(request, 'index.html')


def task_list(request):
    tasks = [{"id": task.id,
              "title": task.title,
              "completed": task.completed,
              'position': task.order} for task in Task.objects.all()]
    return JsonResponse(status=200, data=tasks, safe=False)


def create_task(request):
    title = request.POST.get('title')
    if not title:
        return JsonResponse(status=400, data={'error': 'title is required'})
    task = Task.objects.create(title=title)
    return JsonResponse(status=201, data={'title': task.title,
                                          'completed': task.completed,
                                          'id': task.id,
                                          'position': task.order}, safe=False)


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return JsonResponse(status=204, data={'message': 'task deleted'})


def update_task_status(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    status = request.POST.get('status')
    if not status:
        return JsonResponse(status=400, data={'error': 'status is required'})
    task.completed = int(status)
    task.save()
    return JsonResponse(status=204, data={'message': 'task status updated'})


def update_task_order(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    order = request.POST.get('position')
    if not order:
        return JsonResponse(status=400, data={'error': 'position is required'})
    task.to(int(order))
    return JsonResponse(data={"message": "position updated"}, status=200)

