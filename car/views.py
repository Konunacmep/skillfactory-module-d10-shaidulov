from django.http import request
from django.views.generic.list import ListView
from django.views.generic.edit import FormMixin
from .models import Car
from .forms import CarForm
from django.db.models import Q

class CarFormView(FormMixin, ListView):
    model = Car
    paginate_by = 20
    template_name = 'cars_list.html'
    form_class = CarForm

    def get_queryset(self):
        result_querry = {}
        if self.request.GET.get('year'):
            result_querry[f"year{self.request.GET.get('year_choices', '')}"] = self.request.GET.get('year')
        if self.request.GET.get('color_checked'):
            result_querry['color'] = self.request.GET.get('color')
        if self.request.GET.get('gearbox') and self.request.GET.get('gearbox') != '4':
            result_querry['gearbox'] = self.request.GET.get('gearbox')
        if self.request.GET.get('manufacturer'):
            result_querry['manufacturer__icontains'] = self.request.GET.get('manufacturer')
        if self.request.GET.get('car_model'):
            result_querry['car_model__icontains'] = self.request.GET.get('car_model')
        if result_querry:
            self.initial = self.request.GET
            return Car.objects.filter(Q(**result_querry))
        return Car.objects.all()
