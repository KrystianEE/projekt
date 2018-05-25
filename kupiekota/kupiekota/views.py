from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'index.html'


class InView(TemplateView):
    template_name = 'in.html'


class OutView(TemplateView):
    template_name = 'out.html'
