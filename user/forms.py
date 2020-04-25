from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=15, label='kullanıcı_adı:')
    password = forms.CharField(label='parola',max_length=20, widget= forms.PasswordInput)
    control_password = forms.CharField(label='parola_doğrulama', widget= forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        control_password = self.cleaned_data.get("control_password")

        if password and control_password and password != control_password:
            forms.ValidationError("parolalar eşleşmiyor..")
        else:
            values = {
                "username":username,
                "password":password,
            }
            return values

class SigninForm(forms.Form):
    username = forms.CharField(label='kullanıcı adı:')
    password = forms.CharField(label='parola', widget= forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        values = {
            "username" : username,
            "password" : password,
        }
        return values