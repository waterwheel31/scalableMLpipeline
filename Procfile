git init
dvc config core.no_scm true
dvc pull
web: uvicorn main:app --host=0.0.0.0 --port=${PORT:-5000}