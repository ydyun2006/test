from django.views.generic.base import TemplateView

class Indexview(TemplateView):
    template_name = 'index.html'