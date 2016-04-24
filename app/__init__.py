# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy



app = Flask(__name__) #создаётся объект приложения (наследуя Flask)
app.config.from_object('config')
db = SQLAlchemy(app)
from app import views, models #импорт модуля представления — это обработчики, которые отвечают на запросы веб-браузера.

""" Представления в Flask пишутся как Python функции. Каждая функция представления сопоставляется с одним или несколькими запросами URL """