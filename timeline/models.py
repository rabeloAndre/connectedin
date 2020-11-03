from django.db import models

class Postagem(models.Model):
	texto = models.TextField()
	data_hora = models.DateTimeField(auto_now_add=True)
	perfil = models.ForeignKey('perfil.Perfil',
		related_name = 'postagem',
		on_delete = models.CASCADE)

	class Meta:
		ordering = ['-data_hora']

	def __str__(self):
		return self.texto