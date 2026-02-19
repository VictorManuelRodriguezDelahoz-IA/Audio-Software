# Code Auditor Skill

**Nombre:** code-auditor
**Descripcion:** Audita codigo, revisa calidad, estructura, seguridad y buenas practicas
**Uso:** `/code-auditor [comando]`

---

## Comandos Disponibles

### 1. `/code-auditor audit [proyecto]`
Audita un proyecto completo

**Que hace:**
- Lee estructura de archivos
- Revisa imports, dependencias y configuracion
- Detecta code smells y anti-patterns
- Evalua seguridad (OWASP top 10)
- Verifica buenas practicas de Python/JS/TS
- Genera reporte con scoring

**Ejemplo:**
```
/code-auditor audit recochapp
/code-auditor audit "musica projects"
```

---

### 2. `/code-auditor review [archivo]`
Revisa un archivo especifico en profundidad

**Que hace:**
- Analiza complejidad ciclomatica
- Detecta funciones demasiado largas
- Verifica naming conventions
- Busca vulnerabilidades de seguridad
- Sugiere mejoras concretas

**Ejemplo:**
```
/code-auditor review "musica projects/api/sound_analysis.py"
/code-auditor review Recochapp/backend/main.py
```

---

### 3. `/code-auditor deps [proyecto]`
Audita dependencias y su estado

**Que hace:**
- Lee requirements.txt / package.json
- Verifica versiones desactualizadas
- Detecta dependencias con vulnerabilidades conocidas
- Sugiere actualizaciones
- Identifica dependencias sin usar

**Ejemplo:**
```
/code-auditor deps recochapp
/code-auditor deps "musica projects"
```

---

### 4. `/code-auditor security [proyecto]`
Auditoria de seguridad enfocada

**Que hace:**
- Busca secrets hardcodeados (API keys, passwords)
- Verifica .gitignore (no exponer .env, db files)
- Revisa CORS configuration
- Verifica autenticacion y autorizacion
- Revisa input validation
- Evalua SQL injection, XSS, CSRF risks

**Ejemplo:**
```
/code-auditor security recochapp
/code-auditor security "musica projects"
```

---

### 5. `/code-auditor architecture [proyecto]`
Evalua la arquitectura del proyecto

**Que hace:**
- Mapea estructura de carpetas
- Evalua separacion de concerns
- Verifica patrones (MVC, Clean Architecture, etc.)
- Detecta acoplamiento excesivo
- Sugiere mejoras arquitectonicas

**Ejemplo:**
```
/code-auditor architecture recochapp
```

---

## Formato de Reporte

### Scoring (0-100)

| Dimension | Peso | Que evalua |
|-----------|------|------------|
| Estructura | 20 | Organizacion de archivos y carpetas |
| Calidad de Codigo | 20 | Legibilidad, complejidad, naming |
| Seguridad | 20 | Vulnerabilidades, secrets, input validation |
| Dependencias | 15 | Actualizadas, seguras, necesarias |
| Testing | 15 | Cobertura, calidad de tests |
| Documentacion | 10 | README, docstrings, comentarios utiles |

**Interpretacion:**
- **85-100:** Excelente - Production ready
- **70-84:** Bueno - Necesita mejoras menores
- **50-69:** Aceptable - Necesita trabajo significativo
- **0-49:** Critico - Requiere refactorizacion urgente

### Output Formato

```markdown
# Auditoria de Codigo: [Proyecto]

## Resumen
Score: XX/100
Estado: [Excelente/Bueno/Aceptable/Critico]

## Hallazgos Criticos
- [Issues que deben resolverse YA]

## Hallazgos Importantes
- [Issues que deben resolverse pronto]

## Sugerencias de Mejora
- [Nice-to-have improvements]

## Scoring Detallado
| Dimension | Puntaje | Detalles |
|-----------|---------|----------|

## Plan de Accion
1. [Paso inmediato]
2. [Paso siguiente]
```

---

## Checklist Interno

### Python (FastAPI)
- [ ] Usa type hints
- [ ] Manejo de errores con HTTPException
- [ ] Pydantic models para request/response
- [ ] CORS configurado correctamente
- [ ] Variables de entorno para secrets
- [ ] No hay imports sin usar
- [ ] Funciones < 50 lineas
- [ ] Async donde aplica

### JavaScript/TypeScript (Next.js)
- [ ] TypeScript strict mode
- [ ] No any types
- [ ] Error boundaries
- [ ] Environment variables para API URLs
- [ ] No console.log en produccion
- [ ] Componentes < 200 lineas

### General
- [ ] .gitignore completo
- [ ] .env.example documentado
- [ ] README actualizado
- [ ] Docker/docker-compose funcional
- [ ] No secrets en codigo

---

**Creada:** 2026-02-19
**Version:** 1.0
