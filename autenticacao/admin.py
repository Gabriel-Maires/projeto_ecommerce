from django.contrib import admin
from .models import Usuario, Token, Token_login
from django.contrib.auth import admin as auth_admin
from .forms import UserChangeForm, UserCreationForm



@admin.register(Usuario)
class UsuarioAdmin(auth_admin.UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        ('Sensitive data', {'fields': ('cpf',  'sobrenome', 'cep', 'telefone', 'data_nascimento' )}),
    )




admin.site.register(Token)
admin.site.register(Token_login)