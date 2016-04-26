# -*- coding: utf-8 -*-
import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__) #создаётся объект приложения (наследуя Flask)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models #импорт модуля представления — это обработчики, которые отвечают на запросы веб-браузера.

""" Представления в Flask пишутся как Python функции. Каждая функция представления сопоставляется с одним или несколькими запросами URL """


lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.login_view = 'login'



