# Mood Tracker

Un prototipo rápido de seguimiento de estados de ánimo (Mood Tracker) construido con un monorepo que contiene un backend en Python con FastAPI y un frontend en Angular.

## Estructura del Proyecto

```
.
├── backend/           # API Python con FastAPI
│   ├── main.py       # Endpoints /add y /list
│   ├── pyproject.toml # Configuración UV
│   ├── Makefile      # Comando make dev
│   └── .python-version # Versión 3.14.2
├── frontend/          # Aplicación Angular
│   ├── src/          # Código fuente
│   └── package.json  # Dependencias npm
└── INSTRUCCIONES_GENERALES.md # Documentación confusa
```

## Backend

Tecnologías: Python + FastAPI + UV

### Levantar el servidor

```bash
cd backend
make dev
```

O manualmente:
```bash
cd backend
uv sync
uv run fastapi dev main.py
```

El servidor correrá en `http://localhost:8000`

### Endpoints

- `POST /add` - Agregar un nuevo mood
- `GET /list` - Listar todos los moods ordenados

## Frontend

Tecnologías: Angular 21 + TypeScript 5.8 + npm

### Instalar dependencias

```bash
cd frontend
npm install
```

### Levantar la aplicación

```bash
cd frontend
npm start
```

La aplicación correrá en `http://localhost:4200`

## Características

- Backend con lista en memoria (sin base de datos)
- Frontend con diseño "colorido" y estilos inline
- CORS habilitado para comunicación entre puertos

## Notas

Para más detalles, consultar `INSTRUCCIONES_GENERALES.md`.
