release: python api_pemainBola/manage.py makemigrations --no-input
release: python api_pemainBola/manage.py migrate --no-input

web: gunicorn api_pemainBola.wsgi