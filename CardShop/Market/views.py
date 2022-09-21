from django.shortcuts import render
from django.views.generic.base import View

from .models import MarketCard

class MarketView(View):
    '''Список карт'''
    def get(self, request):
        cards = MarketCard.objects.all()
        return render(request, 'Market/news.html', {'cards':cards})
