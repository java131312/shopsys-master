# -*- coding:utf-8 -*-
"""
Django settings for shopsys project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SETTINGS_DIR = os.path.dirname(__file__)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ao#neh4$it@426fphjeqe$l^#0j7j3ws_lx@_1*c66c9xb-!3t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shopsys.apps.catalog',
    'shopsys.apps.cart',
    'shopsys.apps.login',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'shopsys.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SETTINGS_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'shopsys.utils.context_processors.shopsys',
            ],
        },
    },
]

WSGI_APPLICATION = 'shopsys.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        #  'ENGINE': 'mysql.connector.django', # mysqlclient上这样写的，不需要
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',       # 数据库名
        'USER': 'root',       # 数据库账户名
        'PASSWORD': 'root',  # 数据库密码，为安全起见，应从系统环境变量读取
                                 # 例如os.environ['SHOPSYS_DB_PASS']
        'HOST': '127.0.0.1',     # 数据库服务器IP
        'PORT': '3306',          # 数据库服务端口
        'TEST': {}               # 测试数据库配置

    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

DATE_FORMAT = 'Y-m-d'

TIME_ZONE = 'Asia/Shanghai'

# 是否开启国际化支持，不开启时可以不加载翻译模块优化性能
USE_I18N = False

# 本地化格式支持，为True使用系统locale设置显示数字、时间等格式
USE_L10N = False

USE_TZ = True

# 是否设置Etag, 设置etag可以降低网络资源开销，但会增加服务器性能开销
USE_ETAGS = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
# 生产环境静态资源的配置
# https://docs.djangoproject.com/en/1.9/howto/static-files/deployment/

# 在给定的路径中寻找静态资源
STATICFILES_DIRS = (
    os.path.join(SETTINGS_DIR, 'static'),
)
STATIC_URL = '/static/'

# 用户上传文件位置
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# 站点设置
SITE_NAME = '小白购'
META_KEYWORDS = '小白购, 特价男装, 精品女鞋, 计算机图书, 双十一特惠'
META_DESCRIPTION = '''小白购 - 成都最大、最安全的网上交易平台，提供各类服饰、
    美容、家居、数码、话费/点卡充值… 2亿优质特价商品，同时提供担保交易(先收货
    后付款)、先行赔付、假一赔三、七天无理由退换货、数码免费维修等安全交易保障
    服务，让你全面安心享受网上购物乐趣！'''
