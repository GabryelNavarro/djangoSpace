from django.shortcuts import render, redirect
from usuarios.form import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    form_login = LoginForms()
    return render(request, 'usuarios/login.html', {"form": form_login})

def cadastro(request):
    form_cadastro = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)

        if form.is_valid():
            senha_cadastro_1 = form["senha_cadastro_1"].value()
            senha_cadastro_2 = form["senha_cadastro_2"].value()
            nome = form["nome_cadastro"].value()
            email = form["email_cadastro"].value()

            # Acumula erros nos campos
            if User.objects.filter(email=email).exists():
                form.add_error('email_cadastro', 'E-mail já cadastrado.')

            if senha_cadastro_1 != senha_cadastro_2:
                form.add_error('senha_cadastro_2', 'As senhas não coincidem.')

            if User.objects.filter(username=nome).exists():
                form.add_error('nome_cadastro', 'Nome de usuário já existe.')

            # Se houver erros, renderiza o formulário com todos eles
            if form.errors:
                return render(request, 'usuarios/cadastro.html', {"form": form})

            # Se não houver erros, cria o usuário
            usuario = User.objects.create_user(
                username=nome,
                email=email,
                password=senha_cadastro_1
            )
            usuario.save()
            messages.success(request, "Cadastro realizado com sucesso!")
            return render(request, 'usuarios/cadastro.html', {"form": CadastroForms(), "cadastro_sucesso": True})

    return render(request, 'usuarios/cadastro.html', {"form": form_cadastro})