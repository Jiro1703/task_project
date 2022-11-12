from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from task_app.forms import RecordForm
from task_app.models import (
    Record,
    BShop,
)


def index(request):
    bshops = BShop.objects.all()
    records = Record.objects.all()
    context = {
        'bshops': bshops,
        'records': records
    }
    return render(
        request=request,
        template_name='task_app/index.html',
        context=context,
    )


def output_object(request: HttpRequest) -> HttpResponse:
    records = Record.objects.all()
    context = {
        'records': records
    }
    return render(
        request=request,
        template_name='task_app/index.html',
        context=context,
    )


def delete_object(request: HttpRequest, id_for_del: int) -> HttpResponse:
    Record.objects.filter(pk=id_for_del).delete()

    return redirect('task_app:index')


class RecordCreateView(CreateView):
    template_name = 'task_app/create.html'
    form_class = RecordForm
    success_url = reverse_lazy('task_app:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bshops'] = BShop.objects.all()
        return context
