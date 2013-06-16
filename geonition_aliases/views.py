from django.shortcuts import redirect
from django.http import Http404
from django.views.generic import View
from geonition_aliases.models import Alias


class AliasView(View):
    
    def get(self, request, url):
        a = Alias.objects.get(shortcut=url)
        if a:
            return redirect(a.dst)
        else:
            raise Http404()

