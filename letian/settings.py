"""
Django settings for letian project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-pgk%)y+@$&_*n5%#$(qld1su++!vs@b_13do&7goa^^ujc8&^8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'web.apps.WebConfig',   # 注册APP
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware', # 启用 Session 中间层
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'web.middleware.auth.AuthMiddleware',   # 注册中间件：用户如果没有登录过则强行登录
]

ROOT_URLCONF = 'letian.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'letian.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'letian',
        'PORT':"3306",
        "USER":"root",
        "PASSWORD":"123456",
        "HOST":"127.0.0.1"
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

# 中国简体
LANGUAGE_CODE = 'zh-hans'

# Asia/Shanghai 是 东八区(上海时间)
TIME_ZONE = 'Asia/Shanghai'

# 是否启用国际化功能：下面注释是对国际化的一些解读
"""
国际化功能（Internationalization，通常缩写为 i18n）是指使软件或应用程序能够适应多种语言和文化环境的能力。

在国际化的软件或应用程序中，以下是一些常见的方面：
1. **多语言支持**：用户可以选择他们喜欢的语言来显示界面文本、菜单、提示信息等。这意味着应用程序可以提供多种语言的翻译，以便不同语言的用户能够轻松理解和使用。
2. **文化适应性**：除了语言翻译，国际化还考虑了不同文化之间的差异。这包括日期、时间、货币、度量单位等的格式化，以及对不同地区特定习惯和约定的尊重。
3. **可扩展性**：国际化的设计通常考虑到添加新的语言和文化的需求。这样，当需要支持新的语言或地区时，可以相对容易地添加相应的翻译和文化设置。
4. **字符编码支持**：国际化应用程序通常需要处理不同字符集和编码，以正确显示各种语言的文本。
5. **资源分离**：为了实现多语言支持，应用程序的文本资源通常与代码分离。这使得翻译工作更加容易管理和维护。

国际化的目标是让软件或应用程序能够在全球范围内被广泛使用，而无需为每个新的语言和地区重新开发整个项目。它提高了软件的可用性和用户体验，使其能够更好地满足不同用户的需求。

例如，一个国际化的网站可能允许用户在登录后选择他们喜欢的语言，然后显示相应语言的界面和内容。这样，来自不同国家的用户都可以使用他们熟悉的语言与应用程序进行交互。

"""
USE_I18N = True

# 如果 TIME_ZONE 改为了上海时间则需要把 USE_TZ 从True 改为 False
USE_TZ = False

# 更改时区是方便数据库记录当前的时间

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
