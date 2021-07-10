release: python api_pemainBola/manage.py makemigrations --no-input
release: python api_pemainBola/manage.py migrate --no-input

web: gunicorn --chdir api_pemainBola api_pemainBola.wsgi