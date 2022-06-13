from django.urls import path
from chinook.views import AlbumListAPIView, PlaylistListAPIView, ReportDataAPIView, GenreListAPIView, TrackListAPIView, CreateUsersView, UsuariosListAPIView, CreateObjJsonView, ObjJsonListAPIView
from django.views.decorators.csrf import csrf_exempt
#from .views import index

urlpatterns = [
   # path('', index),
    path('albums/', AlbumListAPIView.as_view()),
    path('genres/', GenreListAPIView.as_view()),
    path('tracks/', TrackListAPIView.as_view()),
    path('playlists/', PlaylistListAPIView.as_view()),
    path('report_data/', ReportDataAPIView.as_view()),
    path('customer_simplified/', csrf_exempt(CreateUsersView.as_view())), #Questão 4
    path('list_customers/', UsuariosListAPIView.as_view()),
    path('obj_Json/', CreateObjJsonView.as_view()), #Questão 6 
]


