# Test Generator Skill

**Nombre:** test-generator
**Descripcion:** Genera y ejecuta tests unitarios, de integracion y E2E para los proyectos
**Uso:** `/test-generator [comando]`

---

## Comandos Disponibles

### 1. `/test-generator generate [proyecto]`
Genera tests para un proyecto completo

**Que hace:**
- Analiza el codigo del proyecto
- Identifica funciones/endpoints sin tests
- Genera tests unitarios con pytest (Python) o Jest (JS/TS)
- Crea fixtures y mocks necesarios
- Organiza tests en estructura estandar

**Ejemplo:**
```
/test-generator generate "musica projects"
/test-generator generate recochapp
```

---

### 2. `/test-generator unit [archivo]`
Genera tests unitarios para un archivo especifico

**Que hace:**
- Lee el archivo fuente
- Identifica todas las funciones/clases
- Genera test cases: happy path, edge cases, error cases
- Crea mocks para dependencias externas
- Incluye parametrize para multiples inputs

**Ejemplo:**
```
/test-generator unit "musica projects/services/sound_processor.py"
/test-generator unit Recochapp/backend/routers/matches.py
```

---

### 3. `/test-generator api [proyecto]`
Genera tests de integracion para endpoints API

**Que hace:**
- Detecta todos los endpoints (FastAPI routes)
- Genera tests con TestClient (FastAPI) o supertest (Express)
- Cubre: GET, POST, PUT, DELETE
- Tests de autenticacion (con/sin token)
- Tests de validacion (inputs invalidos)
- Tests de error handling

**Ejemplo:**
```
/test-generator api "musica projects"
/test-generator api recochapp
```

---

### 4. `/test-generator run [proyecto]`
Ejecuta los tests existentes y reporta resultados

**Que hace:**
- Detecta framework de testing (pytest, jest, vitest)
- Instala dependencias de testing si faltan
- Ejecuta tests con verbose output
- Genera reporte de cobertura
- Sugiere tests faltantes

**Ejemplo:**
```
/test-generator run "musica projects"
/test-generator run recochapp
```

---

### 5. `/test-generator coverage [proyecto]`
Analiza cobertura de tests y sugiere que falta

**Que hace:**
- Ejecuta tests con coverage
- Identifica archivos sin cobertura
- Muestra funciones no testeadas
- Prioriza que testear primero
- Genera plan de testing

**Ejemplo:**
```
/test-generator coverage recochapp
```

---

## Estructura de Tests Generados

### Python (pytest)
```
proyecto/
├── tests/
│   ├── __init__.py
│   ├── conftest.py          # Fixtures compartidas
│   ├── test_main.py         # Tests del entry point
│   ├── unit/
│   │   ├── test_services.py
│   │   └── test_utils.py
│   └── integration/
│       ├── test_api.py
│       └── test_database.py
```

### JavaScript/TypeScript (Jest/Vitest)
```
proyecto/
├── __tests__/
│   ├── setup.ts              # Setup global
│   ├── unit/
│   │   ├── services.test.ts
│   │   └── utils.test.ts
│   └── integration/
│       ├── api.test.ts
│       └── database.test.ts
```

---

## Patrones de Testing

### FastAPI Endpoints
```python
# conftest.py
@pytest.fixture
def client():
    from main import app
    return TestClient(app)

# test_api.py
def test_health_check(client):
    response = client.get("/")
    assert response.status_code == 200

def test_analyze_valid_wav(client, sample_wav):
    response = client.post("/analyze", files={"file": sample_wav})
    assert response.status_code == 200
    assert "frequencies" in response.json()

def test_analyze_invalid_file(client):
    response = client.post("/analyze", files={"file": ("test.txt", b"not audio")})
    assert response.status_code == 400
```

### Coverage Targets
- **Minimo aceptable:** 60%
- **Bueno:** 80%
- **Excelente:** 90%+

---

**Creada:** 2026-02-19
**Version:** 1.0
