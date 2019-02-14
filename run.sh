export DEBUGGER_PORT=5678
export FLASK_APP=app.py
export FLASK_RUN_PORT=8080
export HOST=localhost
export FLASK_ENV=development

python -m ptvsd --host $HOST --port $DEBUGGER_PORT -m flask run --host=$HOST --no-debugger