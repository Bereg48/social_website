from django import forms


class LoginForm(forms.Form):
    """Класс LoginForm осуществляет аутентификацию
пользователей по базе данных, что для прорисовки
HTML-элемента password используется виджет PasswordInput. Это
позволяет вставлять type="password" в HTML, чтобы браузер воспринимал его
как ввод пароля.
"""
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
