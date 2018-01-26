from django import forms
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)
User = get_user_model()
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
        return super(UserLoginForm, self).clean(*args, **kwargs)

#This is a model that will be used to store some of the new registries
class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label="Email address", widget=forms.TextInput(attrs={'class':'form-control'}))
    email2 = forms.EmailField(label="Confirm Email", widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length = 20, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password'
        ]
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError("Emails do not match!")

        return email

            