from re import template
from django.urls import path, include, re_path
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chinook.urls')),
    #path('api-auth/', include('rest_framework.urls'))
]



#urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]


