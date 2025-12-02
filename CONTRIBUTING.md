# 🤝 Guía de Contribución - MindGraphDB

¡Gracias por tu interés en contribuir a MindGraphDB! Este documento te guiará a través del proceso.

## 🎯 Formas de Contribuir

- 🐛 Reportar bugs
- 💡 Sugerir nuevas funcionalidades
- 📝 Mejorar la documentación
- 🔧 Arreglar issues existentes
- ✨ Implementar nuevas características

---

## 🚀 Proceso de Contribución

### 1. Fork y Clone

```bash
# Fork el repositorio en GitHub
# Luego clona tu fork
git clone https://github.com/tu-usuario/MindGraphDB.git
cd MindGraphDB

# Agrega el repositorio original como remote
git remote add upstream https://github.com/original-usuario/MindGraphDB.git
```

### 2. Crea una Rama

```bash
# Actualiza tu main
git checkout main
git pull upstream main

# Crea una nueva rama
git checkout -b feature/nueva-funcionalidad
# o
git checkout -b fix/nombre-del-bug
```

### 3. Realiza tus Cambios

- Escribe código limpio y documentado
- Sigue las convenciones de estilo del proyecto
- Agrega tests si es aplicable
- Actualiza la documentación

### 4. Commit

```bash
# Usa mensajes descriptivos
git add .
git commit -m "Add: implementación de búsqueda avanzada"
```

**Convención de Commits:**
- `Add:` nueva funcionalidad
- `Fix:` corrección de bug
- `Update:` actualización de código existente
- `Docs:` cambios en documentación
- `Test:` agregar o modificar tests
- `Refactor:` refactorización de código

### 5. Push y Pull Request

```bash
# Push a tu fork
git push origin feature/nueva-funcionalidad

# Crea un Pull Request en GitHub
```

---

## 📋 Estándares de Código

### Python (Backend)

```python
# Usa Black para formateo
black backend/

# Usa flake8 para linting
flake8 backend/

# Usa mypy para type checking
mypy backend/
```

### JavaScript (Frontend)

```bash
# Usa Prettier para formateo
npm run format

# Usa ESLint para linting
npm run lint
```

---

## 🧪 Testing

### Backend

```bash
cd backend
pytest tests/ -v --cov=app
```

### Frontend

```bash
cd frontend
npm test
npm run test:coverage
```

---

## 📚 Documentación

- Documenta todas las funciones y clases
- Actualiza el README si es necesario
- Agrega ejemplos de uso

---

## ✅ Checklist antes de PR

- [ ] El código sigue las convenciones de estilo
- [ ] Los tests pasan correctamente
- [ ] La documentación está actualizada
- [ ] Los commits tienen mensajes descriptivos
- [ ] No hay conflictos con la rama main

---

## 🎓 Recursos

- [Guía de Python](https://pep8.org/)
- [Guía de React](https://react.dev/learn)
- [Git Best Practices](https://git-scm.com/book/en/v2)

---

¡Gracias por contribuir a MindGraphDB! 🧠
