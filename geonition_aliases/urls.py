from django.conf.urls.defaults import *
from geonition_aliases.views import AliasView

urlpatterns = patterns('',
    (r'^(?P<url>\w+)/?$', AliasView.as_view()),
    
)