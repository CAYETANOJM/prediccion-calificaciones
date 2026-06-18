# Despliegue del modelo de math score

Aplicacion Flask para desplegar el modelo entrenado con `StudentsPerformance.csv`.

## Ejecutar localmente

```bash
pip install -r requirements.txt
python app.py
```

Despues abre:

```text
http://127.0.0.1:5000/
```

## Despliegue en Render

El archivo `Procfile` ya contiene el comando requerido:

```text
web: gunicorn app:app
```
