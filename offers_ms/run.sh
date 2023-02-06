export FLASK_APP=offers_ms.app.py
export FLASK_DEBUG=1
export FLASK_ENV=development

sudo ufw allow 5003
gunicorn --bind 0.0.0.0:5003 wsgi:offers_ms.app.py

