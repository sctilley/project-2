from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import League

def home(request):
	return render(request, 'tracker/home.html')

class LeagueListView(ListView):
	model = League
	template_name = 'tracker/home.html'
	context_object_name = 'leagues'
	ordering = ['-date']


class LeagueDetailView(DetailView):
	model = League


class LeagueCreateView(LoginRequiredMixin, CreateView):
    model = League
    fields = ['mformat', 'deck', 'record']
    success_url = '/'

    def form_valid(self, form):
    	form.instance.player = self.request.user
    	return super().form_valid(form)

class LeagueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = League
    fields = ['mformat', 'deck', 'record']
    success_url = '/'

    def form_valid(self, form):
    	form.instance.player = self.request.user
    	return super().form_valid(form)

    def test_func(self):
    	league = self.get_object()
    	if self.request.user == league.player:
    		return True
    	return False

class LeagueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = League
	success_url = '/'

	def test_func(self):
		league = self.get_object()
		if self.request.user == league.player:
			return True
		return False


def about(request):
	return render(request, 'tracker/about.html')