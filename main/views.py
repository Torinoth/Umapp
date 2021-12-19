from django.views import generic
from .models import UmaGirl


class IndexView(generic.TemplateView):
    template_name = "index.html"


class UmaGirlListView(generic.ListView):
    model = UmaGirl
    template_name = r"umaGirl\UmaGirlsList.html"


class UmaGirlDetailView(generic.DetailView):
    model = UmaGirl
    template_name = r"umaGirl\UmaGirlDetail.html"
