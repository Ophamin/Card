from django.contrib import admin
from .models import MarketCard, Rating, RatingStar, Replicas, Reviews, Category

admin.site.register(MarketCard)
admin.site.register(Rating)
admin.site.register(RatingStar)
admin.site.register(Replicas)
admin.site.register(Reviews)
admin.site.register(Category)
