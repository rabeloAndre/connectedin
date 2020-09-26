from django.shortcuts import render
from perfil.models import Perfil
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index(request):
	perfil = Perfil.objects.all()
	paginator = Paginator(perfil,5)

	try:
		page = int(request.GET.get('page','1'))
	except:
		page = 1

	try:
		perfil = paginator.page(page)
	except:
		perfil = paginator.page(paginator.num_pages)

	return render(request, 'index.html',{'perfil' : perfil})

def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	return render(request, 'perfil.html',{'perfil' : perfil})

def convidar(request, perfil_id):
	perfil_convidado = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidado)
	return redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)
