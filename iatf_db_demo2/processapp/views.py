from django import http
from django.shortcuts import render
from iatf_db_demo2.processapp.models import Process


def index(request):
    all_steps = Process.objects.all()

    context = {
        'process_steps': all_steps,
    }

    return render(request, 'index.html', context)


def show_page_2(request):
    # specific_step = Process.objects.get(pk=1)
    all_steps = Process.objects.all()
    result = ', '.join([f'{s.step_name} - {s.responsible}' for s in all_steps])
    return http.HttpResponse(result)
