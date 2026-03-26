from django.urls import path
from . import views

urlpatterns = [
    path('customer/', views.customers, name='customers'),
    path('actor/', views.actors, name='actor'),
    path('detalhes/<int:id>', views.detalhes, name='myDetalhe'),
    path('detalhes_filmes/<int:id>', views.detalhes_filmes, name='myDetalheFilm'),
    path('edite/<int:id>/', views.edite, name="edite"),
    path('edite_ator/<int:id>/', views.edite_ator, name="myactors"),
    path('categorias/', views.list_categories, name="categories"),
    path('add_categorias', views.add_category, name="list_categories"),
    path('linguas/', views.list_languages, name="linguagens"),
    path('add_linguas', views.add_language, name="add_languages"),
    path('lista_customer', views.customers_lista, name="lista_customer"),
    path('lista_customer1/', views.customers_lista1, name="lista_customer"),
    path('filter_actor/', views.filter_text_actor, name='filter_actor'),
    path('listacustomerstatic/', views.listacustomerstatic, name='listacustomerstatic'),
    path('listacountry/', views.listacountry, name="listacountry"),
    path('customer_form/', views.customer_form_view, name='customer_form_view'),
    path('salva', views.salva, name='salva'),
    path('category_form/', views.category_form, name='category_form'),

     # search + form category (edite e adcione)
    path('lista_category_form/', views.lista_category_form, name='lista_category_form'),
    path('add_category/', views.add_category, name="add_category"),
    path('edit_category_form/<int:id>/', views.edit_category, name="edit_category"),

    # search + form (edite e adcione)
    path('add_customer/', views.add_customer, name="add_customer"),
    path('edit_customer/<int:id>/', views.edit_customer, name="edit_customer"),
    path('lista_customer_form/', views.lista_customer_form, name='lista_customer_form'),

    #cadastrar usuario
    path('cadastrar_usuario', views.cadastrar_usuario, name="cadastrar_usuario"),
    path('logar_usuario', views.logar_usuario, name="logar_usuario"),
    path('logado', views.logado, name="logado"),
    path('logout/', views.deslogar_usuario, name='logout'),
    path('alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('', views.home, name='home'),

]