from django.shortcuts import render
from django.views.generic import View

from .utils import yelp_search, get_client_data


class IndexView(View):

    def get(self, request, *args, **kwargs):
        items = []
        location = None

        while not location:
            ret = get_client_data()
            if ret:
                location = ret['city']      # Randomic city

        key = request.GET.get('key', None)
        user_location = request.GET.get('loc', None)

        context = {
            'city': location,
            'search': False
        }

        if user_location:
            location = user_location

        items = yelp_search(keyword=key, location=location)
        context = {
            'items': items,
            'city': location,
            'search': True
        }
        return render(request, 'index.html', context)
