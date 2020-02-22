from django.urls import path
from . import views
from .views import MatchCreateView, MatchListView, MatchDetailView


urlpatterns = [
    path('', MatchListView.as_view(), name='tracker-home'),
    path('match/<int:pk>/', MatchDetailView.as_view(), name='match-detail'),
    path('about/', views.about, name='tracker-about'),
    path('match/new/', MatchCreateView.as_view(), name='match-create')
]