from django.views.generic import TemplateView, DetailView

from src.portals.admins.models import Project


class HomeView(TemplateView):
    template_name = 'website/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['projects'] = Project.objects.filter(is_completed=False)[:6]
        context['projects_all'] = Project.objects.filter(is_completed=False)
        return context


class ProjectView(DetailView):
    template_name = 'website/project_detail.html'
    queryset = Project.objects.all()
    pk_url_kwarg = 'slug'
