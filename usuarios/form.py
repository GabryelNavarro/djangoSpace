from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label= "Nome de Usuário",
        required=True,
        max_length=100,
         widget= forms.TextInput(
            attrs={
                
                "placeholder":"Nome Login"
            }
        )
    )
    senha=forms.CharField(
        label= "Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
               
                "placeholder":"Digite sua senha"
            }

        )
    )



class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label= "nome completo",
        required=True,
        max_length=100,
         widget= forms.TextInput(
            attrs={
                
                "placeholder":"Nome de Usuário"
            }
        )
    )
    email_cadastro = forms.EmailField(
         label= "E-MAIL",
        required=True,
        max_length=100,
         widget= forms.EmailInput(
            attrs={
                
                "placeholder":"Insira seu E-mail para cadastrar-se em nosso site"
            }
        )
    )
    senha_cadastro_1=forms.CharField(
        label= "Senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
               
                "placeholder":"Digite sua senha escolhida"
            }

        )
    )
    senha_cadastro_2=forms.CharField(
        label= "Cofirme a senha",
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
               
                "placeholder":"Digite Novamente a senha escolhida"
            }

        )
    )
    
