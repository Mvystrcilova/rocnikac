"""
Django settings for rocnikac project.

Generated by 'django-admin startproject' using Django 2.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from keras.models import load_model
from keras.models import model_from_json

import tensorflow as tf

import joblib, pickle
from gensim.models.keyedvectors import KeyedVectors

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '7j=lv$v61q#zzcc#46y)sfus2zlrg0487sbd9g*8%yp80&%atd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'songRecommender.apps.SongrecommenderConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rocnikac.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATICFILES_DIRS = [
     os.path.join(BASE_DIR, "static"),
]
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['%s/templates/' % (PROJECT_DIR), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'rocnikac.wsgi.application'
MP3FILES_DIR = os.path.join(BASE_DIR, 'mp3_files/')
# MEDIA_ROOT = os.path.join(PROJECT_DIR, "mp3_files")
# MEDIA_URL = '/mp3_files/'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'postgres'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD', 'password'),
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/songRecommender/index'

#aby zatim fungovaly maily
EMAIL_DISABLED = False
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
CELERY_BROKER_URL = 'amqp://localhost'
SELECTED_DISTANCE_TYPE = "TF-idf"

# VYMAZAT!!!!!!!
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True


# Distance thresholds
TF_IDF_THRESHOLD = 0
W2V_THRESHOLD = 0
MEL_SPEC_THRESHOLD = 0
PCA_SPEC_THRESHOLD = 0
PCA_MEL_THRESHOLD = 0
MFCC_THRESHOLD = 0
GRU_SPEC_THRESHOLD = 0
GRU_MEL_THRESHOLD = 0
LSTM_MEL_THRESHOLD = 0

# Loading models
json_file = open('rocnikac/models/GRU_Mel_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
GRU_Mel_model= model_from_json(loaded_model_json)
# load weights into new model
GRU_Mel_model.load_weights("rocnikac/models/GRU_Mel_model.h5")
GRU_Mel_graph = tf.get_default_graph()
print("Loaded model from disk")

# GRU_Spec_model = load_model('rocnikac/models/GRU_Spec_model.h5')
# GRU_Spec_model.compile(optimizer='adam', loss='mse')
# json_file = open('rocnikac/models/GRU_Spec_model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# GRU_Spec_model= model_from_json(loaded_model_json)
# # load weights into new model
# GRU_Spec_model.load_weights("rocnikac/models/GRU_Spec_model.h5")
# print("Loaded model from disk")


json_file = open('rocnikac/models/LSTM_Mel_model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
LSTM_Mel_model = model_from_json(loaded_model_json)
# load weights into new model
LSTM_Mel_model.load_weights("rocnikac/models/LSTM_Mel_model.h5")
LSTM_Mel_graph = tf.get_default_graph()
print("Loaded model from disk")

# json_file = open('rocnikac/models/LSTM_Spec_model.json', 'r')
# loaded_model_json = json_file.read()
# json_file.close()
# LSTM_Spec_model = model_from_json(loaded_model_json)
# # load weights into new model
# LSTM_Spec_model.load_weights("LSTM_Spec_model.h5")
# print("Loaded model from disk")

PCA_Spec_model = joblib.load('rocnikac/models/spec_pca_model')
PCA_Mel_model = joblib.load('rocnikac/models/mel_pca_model')
W2V_model = KeyedVectors.load('w2v_subset', mmap='r')
TF_idf_model = pickle.load(open('rocnikac/models/tfidf_model', "rb"))

# Spectrogram settings !!!! DO NOT CHANGE !!!
n_fft = 4410
hop_length = 812
n_mels = 320
n_mfcc = 320
