
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import views as auth_views
from django.db.models import Q
from .models import Entry
from .forms import EntryForm, RegisterForm

class IndexView(generic.TemplateView):
    template_name = 'diary/index.html'

class RegisterView(generic.CreateView):
    template_name = 'diary/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('diary:login')

class LoginView(auth_views.LoginView):
    template_name = 'diary/login.html'

class LogoutView(auth_views.LogoutView):
    next_page = reverse_lazy('diary:index')

class EntryListView(LoginRequiredMixin, generic.ListView):
    model = Entry
    template_name = 'diary/entry_list.html'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q')
        qs = Entry.objects.filter(owner=self.request.user)
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(body__icontains=q) | Q(tags__icontains=q))
        return qs

class EntryDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Entry
    template_name = 'diary/entry_detail.html'

    def test_func(self):
        entry = self.get_object()
        return entry.owner == self.request.user or not entry.is_private

class EntryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Entry
    form_class = EntryForm
    template_name = 'diary/entry_form.html'
    success_url = reverse_lazy('diary:entry_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class EntryUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Entry
    form_class = EntryForm
    template_name = 'diary/entry_form.html'
    success_url = reverse_lazy('diary:entry_list')

    def test_func(self):
        return self.get_object().owner == self.request.user

class EntryDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Entry
    template_name = 'diary/entry_confirm_delete.html'
    success_url = reverse_lazy('diary:entry_list')

    def test_func(self):
        return self.get_object().owner == self.request.user
