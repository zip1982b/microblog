
# -*- coding: utf-8 -*-
""" Это две настройки, которые нужны нашему расширению Flask-WTF.
    CSRF_ENABLED активирует предотвращение поддельных межсайтовых запросов.
    Эта опция сделает приложение более защищенным.
    SECRET_KEY нужен только тогда, когда включен CSRF.
    Он используется для создания криптографического токена, который используется при валидации формы.
    Когда вы пишете свое приложение, убедитесь, что ваш секретный ключ сложно подобрать."""

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]
