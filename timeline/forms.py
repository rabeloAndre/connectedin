from django.forms import ModelForm
from timeline.models import *

class PostagemForm(ModelForm):
	class Meta:
		model = Postagem
		fields = ['texto']