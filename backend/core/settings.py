INSTALLED_APPS += [
    'rest_framework',
    'users',
    'students',
    'academics',
    'finance',
    'bus',
    'features',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}