# api/run.sh

gunicorn --workers 3 --bind 0.0.0.0:8080 --reload api.wsgi:app --timeout 30  --log-level info