from django.shortcuts import render
from perfil.models import *
from django.shortcuts import redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from timeline.models import *
from timeline.forms import *

@login_required
def add_post(request):
	if request.method == 'POST':
		form = PostagemForm(request.POST)
		if form.is_valid():
			model_instance = form.save(commit=False)
			model_instance.perfil = get_perfil_logado(request)
			model_instance.save()
			return redirect('index')
	else:
		form = PostagemForm()
		return render(request, "timeline/add_post.html", {'form': form})

@login_required
def get_perfil_logado(request):
	return request.user.perfil