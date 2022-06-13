from sys import api_version
from urllib import request
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, GenericAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response
from chinook.serializers import AlbumSerializer, GenreSerializer, PlaylistSerializer, TrackSimplifiedSerializer, CustomersSerializer, ObjJsonSerializer, ListCustomersSerializer, ReportDataSerializer
from chinook.models import Album, Genre, Playlist, Track, Customers
from core.utils import sql_fetch_all
from rest_framework.decorators import api_view
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import render


#Para o Frontend
#def index(request):
 #   return render(request, 'index.html')


##*****************************************************************##

class AlbumListAPIView(ListAPIView):
    queryset = Album.objects.select_related('artist').all()
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination

# Como a queryset estava como Album.objects.all() ela retorna todos os dados da tabela, sem nenhum tipo de filtro, então isso é o que pode ter causado lentidão!
# Resolvi o problema de otimização criando um filtro de select_related().all() passando como parâmetro o campo que é ForeignKey com a tabela Artista, logo as queries diminuiram bastante!
# Além do filtro, criei também uma paginação exibindo somente 100 objetos por página, técnica essa muito útil para resolver problemas de otimização.


##*****************************************************************##

class GenreListAPIView(ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    pagination_class = LimitOffsetPagination 

# Vi que no model dessa rota não temos campos ForeignKey  nem ManyToMany, logo não pude utilizar o filtro select_related().all() nem prefetch_related().all()
# Solução que apliquei foi criar paginação, podendo resolver assim a lentidão da grande carga de dados que estava sendo carregada de uma só vez na página.


##*****************************************************************##
 
class PlaylistListAPIView(ListAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    pagination_class = LimitOffsetPagination

# Ao analisar a rota vi que em seu serializer ao invés de está com o fileds assim: fields = ['name'] estava assim: fields = ('name') de forma errada, logo fiz apenas essa alteração e funcionou.

##*****************************************************************##

class TrackListAPIView(ListAPIView):
    queryset = Track.objects.all().prefetch_related('album','media_type','genre').only('id', 'name', 'composer') # Selected only the fields that will be used.
    serializer_class = TrackSimplifiedSerializer
    pagination_class = LimitOffsetPagination 


# Ao analisar essa rota notamos vários problemas, dentre eles é o de que a rota só precisa exibir três campos, mas no serializer está setado dois campos a mais do que o solicitado!
# Outro problema que notei foi que essa model Track tem três campos sendo ForeignKey de outras tabelas e no queryset estava como objects.all(), logo, causando lentidão ao abrir a rota.
# Além disso a rota demora mais de 15 segundos para carregar.
# Minha solução primeiramente foi fazer a filtragem prefetch_related() passando como parâmetros os campos ForeignKey, no serializer setei apenas os três fields solicitados e adicionei paginação para mostrar apenas 100 por páginas!
# Após a solução a rota abre instataneamente.


##*****************************************************************##


class CreateUsersView(CreateAPIView):
    model = Customers
    permission_classes = [
        permissions.AllowAny  #AllowAny é liberado para todos, não exige autenticação.
    ]
    serializer_class = CustomersSerializer
    pagination_class = LimitOffsetPagination


# Rota criada com cadastro de usuário simplificado, setei somente alguns campos obrigatórios no serializer ('id','first_name', 'last_name', 'email', 'phone')
# Fiz validação de e-mail e telefone para não deixar cadastrar email e/ou telefone já existente no banco usando unique=True como parâmetro nos devidos campos do model.


##*****************************************************************##

class UsuariosListAPIView(ListAPIView): #Listando obj da questão 4

    def get_queryset(self):
        queryset = Customers.objects.all()
        return queryset
    serializer_class = CustomersSerializer
    pagination_class = LimitOffsetPagination

##*****************************************************************##

class CreateObjJsonView(CreateAPIView): #Questão06
    model = Customers
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ObjJsonSerializer
    pagination_class = LimitOffsetPagination

# Rota chamada /obj_Json/ criada para a questão 6, nessa rota criei a API que receberá um objeto JSON em uma solicitação POST. Nela contém oc campos solitiados
# Criei também as verificações de ano min 1970 e ano max 2100 no próprio serializer com positive_only_validator.

##*****************************************************************##

class ObjJsonListAPIView(ListAPIView): #Feito só para teste.
    
    def get_queryset(self):
        queryset = Customers.objects.all()
        return queryset
    serializer_class = ObjJsonSerializer
    pagination_class = LimitOffsetPagination

##*****************************************************************##


#class ReportDataAPIView(GenericAPIView):
 #   def get(self, request, *args, **kwargs):
        
  #      dado = sql_fetch_all(
   #         """
    #          SELECT c.CustomerId, c.FirstName   || ' ' ||  c.LastName as FullName, c.Company, c.Address, c.City, c.State, c.Country, c.Phone, c.PostalCode, c.Email from customers c ORDER BY FullName;
         #   """
        #)

        #return Response(dado)


##*****************************************************************##

class ReportDataAPIView(ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Customers.objects.raw("SELECT c.CustomerId, c.FirstName   || ' ' ||  c.LastName as FullName, c.Company, c.Address, c.City, c.State, c.Country, c.Phone, c.PostalCode, c.Email from customers c ORDER BY CustomerId;")
    serializer_class = ReportDataSerializer
    pagination_class = LimitOffsetPagination


# Nessa questão primeiramente entendi a rota que deveria retornar apenas dados dos clientes, porém ao analisar e testar o código sql notei que o código estava relacionando a tabela de funcionário, o que não queremos!
# Devido a esse erro estava retornando todos os campos da tabela cliente e todos da tabela de funcionários, com isso poder ter causado esse erro de dados ao longo do processo.
# Para resolver eu criei uma nova querie em sql puro na qual ele só captura os campos do cliente de uma forma mais eficiente, alterei a estrutura da view para ListAPIView e criei seu serializer, que era algo que não tinha!
# Além disso, apliquei também a paginação. 

##*****************************************************************##
