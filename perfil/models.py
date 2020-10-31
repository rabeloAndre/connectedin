from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
	nome = models.CharField(max_length=255, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=80, null=False)
	sobre = models.CharField(max_length=255, null=False)
	contatos = models.ManyToManyField('self')
	usuario = models.OneToOneField(User,
		related_name='perfil', on_delete = models.CASCADE)

	@property
	def email(self):
		return self.usuario.email

	def convidar(self, perfil_convidado):
		convite = Convite(solicitados=self,
							recebidos=perfil_convidado)
		convite.save()

class Convite(models.Model):
	solicitados = models.ForeignKey(Perfil,
		related_name = 'convites_feitos',
		on_delete = models.CASCADE)
	recebidos = models.ForeignKey(Perfil, 
		related_name = 'convites_recebidos',
		on_delete = models.CASCADE)

	def aceitar(self):
		self.recebidos.contatos.add(self.solicitados)
		self.solicitados.contatos.add(self.recebidos)
		self.delete()

	def rejeitar(self):
		self.delete()
