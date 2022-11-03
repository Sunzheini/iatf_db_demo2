from django import http
from django.shortcuts import render, redirect
from iatf_db_demo2.processapp.forms import ProcessForm
from iatf_db_demo2.processapp.models import Process


def index(request):
    all_steps = Process.objects.all()

    # ProcessForm
    step_name = None
    responsible = None
    evidence = None
    if request.method == 'GET':
        process_form = ProcessForm()
    else:
        process_form = ProcessForm(request.POST)
        process_form.is_valid()
        step_name = process_form.cleaned_data['step_name']
        responsible = process_form.cleaned_data['responsible']
        evidence = process_form.cleaned_data['evidence']
        Process.objects.create(
            step_name=step_name,
            responsible=responsible,
            evidence=evidence,
        )

    context = {
        'process_steps': all_steps,
        'form': process_form,
        'step_name': step_name,
        'responsible': responsible,
        'evidence': evidence,
    }
    return render(request, 'index.html', context)


def show_page_2(request):
    # specific_step = Process.objects.get(pk=1)
    all_steps = Process.objects.all()
    result = ', '.join([f'{s.step_name} - {s.responsible}' for s in all_steps])
    return http.HttpResponse(result)
