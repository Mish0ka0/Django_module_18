from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class StartList(TemplateView):
    template_name = 'second_task/class_template.html'


def start_str(request):
    return render(request, 'second_task/func_template.html')
