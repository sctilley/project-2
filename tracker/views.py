from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Match

def home(request):
	return render(request, 'tracker/home.html')

def about(request):
	return render(request, 'tracker/about.html')


class MatchListView(ListView):
    model = Match
    template_name = 'tracker/home.html'
    context_object_name = 'matches'
    ordering = ['-date']


class MatchDetailView(DetailView):
    model = Match

class MatchCreateView(LoginRequiredMixin, CreateView):
    model = Match
    fields = ['mformat', 'deck', 'oppdeck', 'record']
    success_url = '/'

    def form_valid(self, form):
        form.instance.player = self.request.user
        return super().form_valid(form)