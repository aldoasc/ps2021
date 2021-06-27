from django.forms import ModelForm
from .models import Usuario

class formUsuario(ModelForm):
	class meta:
		model = Usuario
		fields = '__all__'