# -*- coding: utf-8 -*-
""" Представления в Flask пишутся как Python функции. Каждая функция представления сопоставляется с одним или несколькими запросами URL """
from app import app
from flask import render_template, flash, redirect
from forms import LoginForm


@app.route('/')
@app.route('/index') # два декоратора route создают привязку адресов / и /index к этой функции.
def index():
    user = { 'nickname': 'Zhan' } # выдуманный пользователь
    posts = [ # список выдуманных постов
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title = 'Home', user = user, posts = posts)


# функция представления index опущена для краткости




@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="' + form.openid.data + '", remember_me=' + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title = 'Sign In', form = form, providers = app.config['OPENID_PROVIDERS'])


