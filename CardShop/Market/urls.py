from django.urls import path
from .views import MarketView
urlpatterns = [
    path('', MarketView.as_view(), name='market'),
]
