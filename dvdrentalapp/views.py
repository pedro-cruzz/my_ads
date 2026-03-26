from django.http import HttpResponse
from django.template import loader
from .models import Customer , Actor , Rental, Film, Category, Language, Country

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import CustomerForm, CategoryForm


def customers(request):
    mycustomers = Customer.objects.all().values()
    template = loader.get_template('all_customers.html')
    context = {
        'mycustomer': mycustomers,
    }
    return HttpResponse(template.render(context, request))

def detalhes(request, id):
    myDetalhes = Rental.objects.filter(customer_id=id)
    customer = get_object_or_404(Customer, pk=id)

    template = loader.get_template('detalhes.html')
    context = {
        'myDetalhes': myDetalhes,
        'customer_name': f"{customer.first_name} {customer.last_name}",
        'customer_active': customer.activebool,
        'customer_email' : customer.email
    }
    return HttpResponse(template.render(context, request))

def edite(request, id):
    mycustomer = get_object_or_404(Customer, pk=id)

    if request.method == "POST":
        mycustomer.first_name = request.POST.get('first_name')
        mycustomer.last_name = request.POST.get('last_name')
        mycustomer.email = request.POST.get('email')

        # Atualize outros campos conforme necessário
        mycustomer.save()
        return redirect('/customer')
    return render(request, 'edite.html', {'mycustomer': mycustomer,})

def actors(request):
    myactors = Actor.objects.all().values()
    template = loader.get_template('all_actors.html')
    context = {
        'myactor': myactors,
    }
    return HttpResponse(template.render(context, request))

def detalhes_filmes(request, id):
    myDetalhesFilm = Film.objects.filter(film_id=id)
    myDetalheActor = Actor.objects.filter(actor_id=id)
    film = get_object_or_404(Film, pk=id)

    template = loader.get_template('detalhes_actors.html')
    context = {
        'myDetalheActor': myDetalheActor,
        'myDetalheFilm': myDetalhesFilm,
        'actor_name': f"{film.title} {film.description}",
    }
    return HttpResponse(template.render(context, request))

def edite_ator(request, id):
    myactor = get_object_or_404(Actor, pk=id)

    if request.method == "POST":
        myactor.first_name = request.POST.get('first_name')
        myactor.last_name = request.POST.get('last_name')

        # Atualize outros campos conforme necessário
        myactor.save()
        return redirect('/actor')
    return render(request, 'edite_actors.html', {'myactor': myactor,})

def list_categories(request):
    categories = Category.objects.all()
    return render(request, 'list_categories.html', {'categories': categories})

def add_category(request):
    if request.method == "POST":
        name = request.POST.get('name')

        # Cria uma instância do modelo Category e salva no banco
        category = Category(name=name, last_update=timezone.now())
        category.save()

        # Redireciona para a lista de categorias após a inserção
        return redirect('/categorias')  

    # Se não for um POST request, exibe o formulário vazio
    return render(request, 'add_category.html')


def list_languages(request):
    languages = Language.objects.all()
    return render(request, 'list_language.html', {'languages': languages})

def add_language(request):
    if request.method == "POST":
        name = request.POST.get('name')

        # Cria uma instância do modelo Category e salva no banco
        language = Language(name=name, last_update=timezone.now())
        language.save()

        # Redireciona para a lista de categorias após a inserção
        return redirect('/linguas')  

    # Se não for um POST request, exibe o formulário vazio
    return render(request, 'add_language.html')


def customers_lista(request): #para usar o contains
    mycustomerlistacontains = Customer.objects.filter(first_name__contains='Karen').values()
    mycustomerlistaicontains = Customer.objects.filter(last_name__icontains='Mill').values()
    mycustomerlistaendswith = Customer.objects.filter(first_name__endswith='s').values() # case sensitive exatamente com "s" minúsculo
    mycustomerlistaiendswith = Customer.objects.filter(first_name__iendswith='S').values() # Case-insensitive ignora maiúsculas/minúsculas
    mycustomerlistaexact = Customer.objects.filter(first_name__exact='Phyllis').values() # case sensitive exatamente como esta escrito
    mycustomerlistaiexact = Customer.objects.filter(first_name__iexact='phyllis').values() # case sensitive ignora maiúsculas/minúsculas
    mycustomerlistain = Customer.objects.filter(first_name__in=['Phyllis', 'Dennis', 'Nicholas']).values()
    mycustomerlistagt = Customer.objects.filter(customer_id__gt=500).values() # > 500
    mycustomerlistagte = Customer.objects.filter(customer_id__gte=550).values() # >= 700
    mycustomerlistalt = Customer.objects.filter(customer_id__lt=10).values() # < 500
    mycustomerlistalte = Customer.objects.filter(customer_id__lte=10).values() # <= 700
    template = loader.get_template('list_customer.html')
    context = {
        'mycustomerlistacontains': mycustomerlistacontains,
        'mycustomerlistaicontains': mycustomerlistaicontains,
        'mycustomerlistaendswith': mycustomerlistaendswith,
        'mycustomerlistaiendswith': mycustomerlistaiendswith,
        'mycustomerlistaexact': mycustomerlistaexact,
        'mycustomerlistaiexact': mycustomerlistaiexact,
        'mycustomerlistain': mycustomerlistain,
        'mycustomerlistagt': mycustomerlistagt,
        'mycustomerlistagte': mycustomerlistagte,
        'mycustomerlistalt': mycustomerlistalt,
        'mycustomerlistalte': mycustomerlistalte,

    }
    return HttpResponse(template.render(context, request))

def customers_lista1(request):
    mycustomersand = Customer.objects.filter(first_name='Maria', customer_id=7).values() # AND
    mycustomersor = Customer.objects.filter(first_name='Maria').values() | Customer.objects.filter(customer_id=8).values() # OR
    template = loader.get_template('list_customer1.html')
    context = {
        'mycustomersand': mycustomersand,
        'mycustomersor':mycustomersor,
    }
    return HttpResponse(template.render(context, request))

# search + form
def lista_customer_form(request):
    # Obtém o valor de 'search_name' da requisição GET, retorna None se não encontrado
    search_name = request.GET.get('search_name', '')

    if search_name:
        # Filtra os clientes pelo nome fornecido
        lista_customer_form = Customer.objects.filter(first_name__contains=search_name).values()
    else:
        # Retorna todos os clientes se nenhum nome for fornecido
        lista_customer_form = Customer.objects.all().values()

    template = loader.get_template('lista_customer_form.html')
    context = {
        'lista_customer_form': lista_customer_form,
    }
    return HttpResponse(template.render(context, request))

def edit_customer(request, id):
    customer = get_object_or_404(Customer, pk=id)

    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('lista_customer_form')
    else:
        form = CustomerForm(instance=customer)

    context = {
        'form': form,
    }

    return render(request, 'edite_customer.html', context)

def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_customer_form')
    else:
        form = CustomerForm()

    context = {
        'form': form,
    }

    return render(request, 'adicionar_customer.html', context)


def filter_text_actor(request):
    # Obtém o valor de 'search_name' da requisição GET, retorna None se não encontrado
    search_name = request.GET.get('search_name', '')

    if search_name:
        # Filtra os clientes pelo nome fornecido
        filter_text_actor = Actor.objects.filter(first_name__contains=search_name).values()
    else:
        # Retorna todos os clientes se nenhum nome for fornecido
        filter_text_actor = Actor.objects.all().values()

    template = loader.get_template('filter_text_actors.html')
    context = {
        'filter_text_actor': filter_text_actor,
    }
    return HttpResponse(template.render(context, request))

def listacustomerstatic(request):
    mycustomersstatic = Customer.objects.all().values()
    template = loader.get_template('list_customer_static.html')
    context = {
        'mycustomersstatic': mycustomersstatic,
    }
    return HttpResponse(template.render(context, request))

def listacountry(request):
    country = Country.objects.all().values()
    template = loader.get_template('list_country.html')
    context = {
        'listcountry': country,
    }
    return HttpResponse(template.render(context, request))

def customer_form_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salva')
    else:
        form = CustomerForm()

    return render(request, 'Customer_form_template.html', {'form': form})

def salva(request):
    return render(request, 'salva.html')

def category_form(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salva')
    else:
        form = CategoryForm()

    return render(request, 'category_form.html', {'form': form})

def salva(request):
    return render(request, 'salva.html')

# form category + search category (edite e adcione)
def lista_category_form(request):
    # Obtém o valor de 'search_name' da requisição GET, retorna None se não encontrado
    search_name = request.GET.get('search_name', '')

    if search_name:
        # Filtra os clientes pelo nome fornecido
        lista_category_form = Category.objects.filter(first_name__contains=search_name).values()
    else:
        # Retorna todos os clientes se nenhum nome for fornecido
        lista_category_form = Category.objects.all().values()

    template = loader.get_template('lista_category_form.html')
    context = {
        'lista_category_form': lista_category_form,
    }
    return HttpResponse(template.render(context, request))

def edit_category(request, id):
    category = get_object_or_404(Category, pk=id)

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('lista_category_form')
    else:
        form = CategoryForm(instance=category)

    context = {
        'form': form,
    }

    return render(request, 'edite_category.html', context)

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_category_form')
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'adicionar_category.html', context)

#cadastrar usuario
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('salva')
    else:
        form_usuario = UserCreationForm()

    return render(request, 'cadastro.html', {'form_usuario': form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('logado')
        else:
            form_login = AuthenticationForm()
    else:
        form_login = AuthenticationForm()

    return render(request, 'login.html', {'form_login': form_login})

def logado(request):
    return render(request, 'logado.html')

@login_required
def deslogar_usuario(request):
    logout(request)
    return redirect('home')

@login_required
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)  # mantém logado
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)

    return render(request, 'alterar_senha.html', {'form_senha': form_senha})


def home(request):
    return render(request, 'home.html')