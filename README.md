# 🧠 MindGraphDB - Sistema Inteligente de Análisis de Salud Mental Estudiantil

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![React](https://img.shields.io/badge/React-18+-61DAFB.svg)](https://reactjs.org/)
[![Neo4j](https://img.shields.io/badge/Neo4j-5.x-008CC1.svg)](https://neo4j.com/)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 📋 Descripción

**MindGraphDB** es una plataforma web inteligente que combina análisis de grafos, machine learning y big data para estudiar patrones de salud mental en estudiantes. Utiliza Neo4j para visualizar relaciones complejas entre factores de depresión y aplica algoritmos de clasificación e indexación para análisis de artículos científicos.

### 🎯 Características Principales

- 📊 **Dashboard Interactivo**: Visualizaciones en tiempo real de datos de salud mental
- 🕸️ **Análisis de Grafos**: Exploración de relaciones usando Neo4j y algoritmos PageRank
- 🔍 **Búsqueda Inteligente**: Sistema de ranking de artículos con TF-IDF
- 🤖 **Machine Learning**: Clasificación predictiva con Naive Bayes y análisis de sentimientos
- 🐳 **Completamente Dockerizado**: Deploy rápido con Docker Compose
- 📈 **Big Data**: Procesamiento eficiente de datasets con pandas

---

## 🏗️ Arquitectura del Sistema

```
┌─────────────────────────────────────────────┐
│         Frontend (React + D3.js)            │
│     Dashboard | Grafos | Búsqueda           │
└──────────────────┬──────────────────────────┘
                   │ REST API
┌──────────────────▼──────────────────────────┐
│         Backend (FastAPI + Python)          │
│   ML Models | NLP | Business Logic          │
└──────────────────┬──────────────────────────┘
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
┌───────────────┐     ┌──────────────┐
│  PostgreSQL   │     │    Neo4j     │
│   (Datos)     │     │   (Grafos)   │
└───────────────┘     └──────────────┘
```

## 🚀 Tecnologías

- **Frontend:** React + TypeScript
- **Backend:** FastAPI (Python)
- **Bases de Datos:** PostgreSQL + Neo4j
- **Contenedores:** Docker + Docker Compose
- **ML/NLP:** scikit-learn, NLTK, VADER

## 📦 Instalación

### Prerrequisitos
- Docker Desktop instalado
- Git

### Paso 1: Clonar repositorio
```bash
git clone https://github.com/tu-usuario/MindGraphDB.git
cd MindGraphDB
```

### Paso 2: Colocar datasets
Coloca los archivos CSV en `data/raw/`:
- `Student Depression Dataset.csv`
- `articles.csv`

### Paso 3: Levantar contenedores
```bash
docker-compose up --build
```

### Paso 4: Acceder a servicios
- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:8000/docs
- **Neo4j Browser:** http://localhost:7474
- **PostgreSQL:** localhost:5432

## 📊 Estructura del Proyecto
```
MindGraphDB/
├── backend/          # API FastAPI
├── frontend/         # React App
├── data/             # Datasets CSV
├── database/         # Scripts SQL/Cypher
└── docs/             # Documentación
```

## 🔧 Desarrollo

### Instalar dependencias backend (local)
```bash
cd backend
pip install -r requirements.txt
```

### Instalar dependencias frontend (local)
```bash
cd frontend
npm install
```

## 📝 Uso

1. Cargar datos: `python backend/scripts/load_data.py`
2. Entrenar modelo: `python backend/scripts/train_model.py`
3. Explorar dashboard en http://localhost:3000

## 📚 Documentación

Ver carpeta `docs/` para arquitectura detallada y guías de uso.

## 🤝 Contribuciones

Pull requests son bienvenidos. Para cambios mayores, abre un issue primero.

## 📄 Licencia

MIT