from django.shortcuts import render, redirect
from .utils import email_html
from django.http import HttpResponse
from django.contrib.messages import constants
from django.contrib import messages
import re
from .models import Usuario as User, Token_login
from .models import Token
import hashlib
from pathlib import Path
from system_manager import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import auth
from django.db.models import Q
from hashlib import sha256
from random import randint
from django.contrib import auth
from django.contrib.auth.decorators import login_required



def cadastro(request):
    if request.user.is_authenticated:
        return redirect('/') 
    if request.method == 'GET':
        return render(request, 'cadastro.html')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            senha = request.POST.get('senha')
            repetir_senha = request.POST.get('repetir_senha')
            sobrenome = request.POST.get('sobrenome')
            cpf = request.POST.get('cpf')
            cep = request.POST.get('cep')
            numero = request.POST.get('numero')
            telefone = request.POST.get('telefone')
            data_nascimento = request.POST.get('data_nascimento')

            if len(username.strip()) == 0 or len(email.strip()) == 0 or len(senha.strip()) == 0 or\
               len(repetir_senha.strip()) == 0 or len(sobrenome.strip()) == 0 or len(cpf.strip()) == 0\
                or len(cep.strip()) == 0 or len(numero.strip()) == 0 or len(telefone.strip()) == 0 \
                or len(data_nascimento.strip())== 0:

                messages.add_message(request, constants.ERROR, 'Nenhum campo pode ser mulo.')
                return redirect('cadastro')

            sobrenome = sobrenome.strip()
            if not sobrenome.isalpha():
                messages.add_message(request, constants.ERROR, 'Insira um sobrenome válido.')
                return redirect('cadastro')

            elif not cep.isnumeric() or not cpf.isnumeric() or not numero.isnumeric() or not telefone.isnumeric():
                messages.add_message(request, constants.ERROR, 'Insira nos campos respectivos dados númericos.')
                return redirect('cadastro')


            elif senha != repetir_senha:
                messages.add_message(request, constants.ERROR, 'Senhas não conferem.')
                return redirect('cadastro')

            elif not re.search('[A-Z]', senha):
                messages.add_message(request, constants.ERROR, 'Sua senha precisa ter letras maiúsculas.')
                return redirect('cadastro')

            elif not re.search('[a-z]', senha):
                messages.add_message(request, constants.ERROR, 'Sua senha precisa ter letras minúsculas' )
                return redirect('cadastro')

            elif len(senha) < 8:
                messages.add_message(request, constants.ERROR, 'Sua senha precisa ter no mínimo 8 caracteres.' )
                return redirect('cadastro')


            
            query = Q(
                Q(email=email)|Q(username=username)
            )
            userr = User.objects.filter(query)
            if len(userr) > 0:
                messages.add_message(request, constants.ERROR, 'Usuário ou email já cadastrados.')
                return redirect('login')

            try:
                user = User.objects.create_user(
                                                username=username,
                                                password=senha,
                                                email=email,
                                                is_active=False,
                                                sobrenome=sobrenome,
                                                cpf=cpf,
                                                cep=cep,
                                                numero=numero,
                                                telefone=telefone,
                                                data_nascimento=data_nascimento
                                                
                                                
                                                )

                user.save()

            except:
                messages.add_message(request, constants.ERROR, 'Erro interno do sistema.Tente novamente em instantes.')
                return redirect('cadastro')
            user_id = User.objects.get(id=user.id)

            token = hashlib.sha256(f'{username}{email}'.encode()).hexdigest()
            try:
                token_usuario = Token(usuario_id=user_id.id, token=token)
                token_usuario.save()

            except:
                pass

            
            
            try:   
                path_template = Path(settings.BASE_DIR, 'autenticacao/templates/email/email.html')
                
                email_html(path_template=path_template, assunto= 'Autentique a sua conta para fazer login no sistema Imobi.', 
                            para=[email,], link_ativacao=f'http://127.0.0.1:8000/auth/ativacao/{token}', usuario=username )
                messages.add_message(request, constants.SUCCESS, 'Você foi cadastrado. Agora Verifique seu email.')
                return redirect('login')
            except:
                messages.add_message(request, constants.ERROR, 'Erro interno do sistema. Tente novamente em instantes.')
                return redirect('cadastro')
        
            


def login(request):
    if request.user.is_authenticated:
        return redirect('/') 

    if request.method == 'GET':
        return render(request,'login.html')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            senha = request.POST.get('senha')
            email = request.POST.get('email')
            print(f'{username} {senha} {email}')

            codigo = str(randint(0,1000000))
        
            usuario = auth.authenticate(username=username, password=senha)
           
            if not usuario:
                messages.add_message(request, constants.ERROR, 'Usuário ou senha inválidos.')
                return redirect('login')
            if usuario:
                token_login = Token_login(user=usuario, login_codigo=codigo)
                token_login.save()

            
        
                path_templatee = Path(settings.BASE_DIR, 'autenticacao/templates/email/authemail.html')
            
                email_html(path_template=path_templatee, assunto= 'Autentique a sua conta para fazer login..', 
                            para=[email,], codigo=codigo, usuario=username )
            
                messages.add_message(request, constants.SUCCESS, 'Verifique o código no seu email.')
                return redirect('autentication')
           

    
          



def sair(request):
    auth.logout(request)
    return redirect('login')

   


def autentication(request):
    if request.user.is_authenticated:
        return redirect('/') 
        
    if request.method == 'GET':
        return render(request, 'autentication.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        code = request.POST.get('code')

        usuario = auth.authenticate(username=username, password=senha)
        print(usuario)
        token_login = Token_login.objects.filter(login_codigo=code)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos.')
            return redirect('login')

        if not token_login:
            messages.add_message(request, constants.WARNING, 'Esse código de verificação já foi utilizado.')
            return redirect('login')

        if usuario and token_login:
        
                auth_user = auth.authenticate(username=username, password=senha) 
                if auth_user:

                    token_login = Token_login.objects.filter(login_codigo=code)[0]
                    token_login.delete()
                    auth.login(request, auth_user)
                    return redirect('/')
        else:
            messages.add_message(request, constants.ERROR, 'Algo deu errado. Tente fazer login novamente.')
            return redirect('login')

        

        




def ativacao(request, token):
    usuario_token = Token.objects.get(token=token)
    usuario_user = User.objects.get(id=usuario_token.usuario.id)

    if usuario_token.validade:
        messages.add_message(request, constants.WARNING, 'Essa conta já foi autenticada.')
        return redirect('cadastro')

    usuario_token.validade = True
    usuario_token.save()

    usuario_user.is_active = True
    usuario_user.save()
    messages.add_message(request, constants.SUCCESS, 'Sua conta está autenticada. Agora faça login.')
    return redirect('login')