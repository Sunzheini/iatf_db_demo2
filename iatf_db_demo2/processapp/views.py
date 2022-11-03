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
        # from form
        'step_name': step_name,
        'responsible': responsible,
        'evidence': evidence,
    }
    return render(request, 'index.html', context)


def overview(request):
    all_steps = Process.objects.all()
    result = ', '.join([f'{s.step_name} - {s.responsible}' for s in all_steps])
    context = {
        'result': result,
    }

    # return http.HttpResponse(result)
    return render(request, 'overview.html', context)


def processes_description(request, process_id):
    specific_step = Process.objects.get(pk=1)   # ToDo hardcoded currently
    context = {
        'specific_step': specific_step,
    }

    # return http.HttpResponse(f"{specific_step.step_name} - {specific_step.responsible}")
    return render(request, 'process_description.html', context)


def redirect_to(request):
    # return redirect('overview')                         # option 1 name of the url in urls.py
    # return redirect('https://www.abv.bg/')
    # return redirect('/processes-description/1/')        # option 2 hardcoded url path

    return redirect('show specific process', process_id=1)     # option 3 for cases like .../pk
