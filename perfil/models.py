from django.db import models

class Perfil(models.Model):
	nome = models.CharField(max_length=255, null=False)
	email = models.EmailField(max_length=100, null=False)
	telefone = models.CharField(max_length=15, null=False)
	nome_empresa = models.CharField(max_length=80, null=False)
	sobre = models.CharField(max_length=255, null=False)

	def convidar(self, perfil_convidado):
		convite = Convite(solicitados=self,
							recebidos=perfil_convidado)
		convite.save()

class Convite(models.Model):
	solicitados = models.ForeignKey(Perfil,
		related_name = 'solicitados',
		on_delete = models.CASCADE)
	recebidos = models.ForeignKey(Perfil, 
		related_name = 'recebidos',
		on_delete = models.CASCADE)
