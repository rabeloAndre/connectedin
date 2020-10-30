from django.shortcuts import render
from perfil.models import Perfil, Convite
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

	return render(request, 'index.html',
				{'perfil' : perfil,
				'perfil_logado' : get_perfil_logado(request)})

def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	eh_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil.html',
				{'perfil' : perfil,
				'perfil_logado' : perfil_logado,
				'eh_contato' : eh_contato})

def convidar(request, perfil_id):
	perfil_convidado = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidado)
	return redirect('index')

def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

def get_perfil_logado(request):
	return Perfil.objects.get(id=1)
