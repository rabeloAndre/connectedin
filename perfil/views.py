from django.shortcuts import render
from perfil.models import Perfil, Convite
from django.shortcuts import redirect
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.contrib.auth.decorators import login_required

@login_required
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

	return render(request, 'perfil/index.html',
				{'perfil' : perfil,
				'perfil_logado' : get_perfil_logado(request)})

@login_required
def exibir(request, perfil_id):
	perfil = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	eh_contato = perfil in perfil_logado.contatos.all()
	return render(request, 'perfil/perfil.html',
				{'perfil' : perfil,
				'perfil_logado' : perfil_logado,
				'eh_contato' : eh_contato})

@login_required
def convidar(request, perfil_id):
	perfil_convidado = Perfil.objects.get(id=perfil_id)
	perfil_logado = get_perfil_logado(request)
	perfil_logado.convidar(perfil_convidado)
	return redirect('index')

@login_required
def aceitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.aceitar()
	return redirect('index')

@login_required
def rejeitar(request, convite_id):
	convite = Convite.objects.get(id=convite_id)
	convite.rejeitar()
	return redirect('index')

@login_required
def get_perfil_logado(request):
	return request.user.perfil
