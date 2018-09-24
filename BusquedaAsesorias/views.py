from django.shortcuts import render
from django.views.generic.list import ListView
from accounts.models import Asesoria, Curso, Profesor

# Create your views here.

def BusquedaAsesorias(request):
    return render(request, 'BusquedaAsesorias.html', {})

class BusquedaAsesoriasView(ListView):
    model = Asesoria
    template_name = "BusquedaAsesorias/forms.html"
    paginate_by = 10

    def get_queryset(self):
        filter_val = self.request.GET.get('filter', 'give-default-value')
        order = self.request.GET.get('orderby', 'give-default-value')
        new_context = Asesoria.objects.filter(
            state=filter_val,
        ).order_by(order)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(MyView, self).get_context_data(**kwargs)
        context['filter'] = self.request.GET.get('filter', 'give-default-value')
        context['orderby'] = self.request.GET.get('orderby', 'give-default-value')
        return context
