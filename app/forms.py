# -*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required  # это валидатор, функция, которая может быть прикреплена к полю, для выполнения валидации данных отправленных пользователем. Валидатор Required просто проверяет, что поле не было отправлено пустым.

class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember_me', default = False)


