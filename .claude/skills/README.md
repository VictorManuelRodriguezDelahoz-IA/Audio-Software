# Skills del Proyecto

## Skills Disponibles

### 1. Business Analyst
Analiza negocios, evalua oportunidades y genera reportes de investigacion.

**Archivo:** [business-analyst.md](business-analyst.md)

### 2. Code Auditor (NUEVO)
Audita codigo, revisa calidad, estructura, seguridad y buenas practicas.

**Archivo:** [code-auditor.md](code-auditor.md)

**Comandos:**
- `/code-auditor audit [proyecto]` - Auditoria completa
- `/code-auditor review [archivo]` - Revision de archivo
- `/code-auditor deps [proyecto]` - Auditoria de dependencias
- `/code-auditor security [proyecto]` - Auditoria de seguridad
- `/code-auditor architecture [proyecto]` - Evaluacion arquitectonica

### 3. Test Generator (NUEVO)
Genera y ejecuta tests unitarios, de integracion y E2E.

**Archivo:** [test-generator.md](test-generator.md)

**Comandos:**
- `/test-generator generate [proyecto]` - Tests para proyecto completo
- `/test-generator unit [archivo]` - Tests unitarios para archivo
- `/test-generator api [proyecto]` - Tests de API/endpoints
- `/test-generator run [proyecto]` - Ejecutar tests existentes
- `/test-generator coverage [proyecto]` - Analisis de cobertura

### 4. Market Researcher (NUEVO)
Investiga mercados, identifica tendencias, analiza competencia y descubre oportunidades.

**Archivo:** [market-researcher.md](market-researcher.md)

**Comandos:**
- `/market-researcher scan [sector]` - Escaneo amplio de sector
- `/market-researcher deep-dive [idea]` - Analisis profundo
- `/market-researcher competitors [producto]` - Mapa competitivo
- `/market-researcher combine [idea1] + [idea2]` - Analisis de combinacion
- `/market-researcher trends [ano]` - Tendencias del ano
- `/market-researcher validate [idea]` - Validacion rapida

---

## 🚀 Cómo Usar las Skills

### Método 1: Invocación Directa (Recomendado)

Simplemente menciona lo que quieres en el chat con Claude:

```
"Analiza el proyecto Recochapp"
"Investiga oportunidades de audio en USA"
"Crea un análisis de la idea 'AI Audio Mastering'"
"Compara Recochapp vs musica projects"
```

Claude automáticamente usará la skill business-analyst para:
- Leer la documentación relevante
- Buscar información en la web
- Generar análisis estructurado
- Crear archivos de reporte

### Método 2: Comando Explícito

También puedes usar comandos específicos:

```
/business-analyst evaluate recochapp
/business-analyst research usa audio
/business-analyst opportunity "AI Audio Mastering"
/business-analyst portfolio
```

---

## 📋 Comandos Disponibles

| Comando | Descripción | Ejemplo |
|---------|-------------|---------|
| `evaluate [proyecto]` | Evalúa proyecto existente | `/business-analyst evaluate recochapp` |
| `research [mercado] [sector]` | Investiga mercado | `/business-analyst research usa audio` |
| `opportunity [idea]` | Analiza idea específica | `/business-analyst opportunity "AI Mastering"` |
| `compare A vs B` | Compara dos opciones | `/business-analyst compare recochapp vs ml-studios` |
| `portfolio` | Analiza portafolio completo | `/business-analyst portfolio` |
| `trends [sector] [año]` | Tendencias del sector | `/business-analyst trends audio 2026` |

---

## 💡 Casos de Uso Prácticos

### 1. Quiero saber si debo continuar con Recochapp

```
Tú: "Evalúa Recochapp y dame tu recomendación"

Claude:
- Lee docs de Recochapp
- Analiza modelo de negocio
- Busca competencia en web
- Calcula scoring
- Da recomendación: Continuar / Pausar / Pivotar
```

### 2. Busco nuevas oportunidades en USA

```
Tú: "Investiga oportunidades de audio tech en Estados Unidos"

Claude:
- Busca tendencias 2026
- Identifica startups con funding
- Detecta pain points
- Lista top 5 oportunidades con scoring
```

### 3. Tengo una idea y quiero validarla

```
Tú: "Analiza la oportunidad de hacer un servicio de AI mastering"

Claude:
- Crea archivo en /docs/oportunidades-negocio/usa/
- Investiga mercado y competencia
- Llena template completo
- Calcula scoring (0-80)
- Recomienda: Priorizar / Investigar / Descartar
```

### 4. No sé qué proyecto hacer después

```
Tú: "Analiza mi portafolio y recomiéndame qué hacer"

Claude:
- Revisa Recochapp + musica projects
- Identifica gaps y sinergias
- Busca oportunidades complementarias
- Recomienda próximo proyecto
```

---

## 📊 Output Generado

### Formato de Análisis

Cada análisis incluye:

```markdown
# Análisis de [Nombre]

## 📊 Resumen Ejecutivo
[2-3 párrafos clave]

## 🎯 Scoring (0-80)
| Dimensión | Puntaje | Justificación |
|-----------|---------|---------------|
| Tamaño de Mercado | 8/10 | ... |
| Innovación | 7/10 | ... |
...
**TOTAL: 65/80** 🟢

## 💪 SWOT Analysis
**Fortalezas:** ...
**Debilidades:** ...
**Oportunidades:** ...
**Amenazas:** ...

## ✅ Recomendación
PRIORIZAR / INVESTIGAR / DESCARTAR

## 🚀 Next Steps
1. [Acción específica]
2. [Acción específica]
...
```

### Archivos Creados

Los análisis se guardan automáticamente en:
- `docs/oportunidades-negocio/[país]/[nombre].md`
- `docs/startup-hq/evaluaciones/[proyecto].md`

---

## 🧠 Inteligencia de la Skill

### Fuentes de Información

1. **Documentación Local:**
   - Lee tus docs de proyectos
   - Analiza roadmaps y modelos de negocio
   - Revisa tus ideas en Notion (sincronizadas)

2. **Web Research:**
   - Google Trends
   - Crunchbase (startups y funding)
   - Y Combinator library
   - Product Hunt
   - Reddit (pain points)
   - Industry reports

3. **Contexto Personal:**
   - Tus skills: Audio, Tech, ML
   - Tu situación: Doctorado en Alemania
   - Tus recursos: Bootstrap vs funding
   - Tus proyectos actuales

### Scoring Inteligente

El scoring considera:
- **Tamaño de mercado:** TAM, SAM, SOM
- **Innovación:** Qué tan único es
- **Ventaja competitiva:** Moats, defensibilidad
- **Viabilidad técnica:** Complejidad, recursos
- **Alineación personal:** Fit con tus skills
- **Potencial de impacto:** Problema que resuelve
- **Time to market:** Velocidad de ejecución
- **Capital requerido:** Inversión necesaria

---

## 🎯 Workflows Recomendados

### Workflow 1: Decisión de Nuevo Proyecto (Mensual)

```
1. /business-analyst portfolio
   → Revisar estado actual

2. /business-analyst research [mercado] [sector]
   → Explorar oportunidades

3. /business-analyst opportunity "[top 3 ideas]"
   → Analizar las mejores

4. /business-analyst compare "[idea A]" vs "[idea B]"
   → Decidir entre finalistas

5. Decisión: Continuar con proyecto actual o iniciar nuevo
```

### Workflow 2: Validación Rápida de Idea (Semanal)

```
1. Tienes una idea
   → "Analiza la oportunidad de [tu idea]"

2. Claude genera análisis completo
   → Scoring + SWOT + Recomendación

3. Si scoring > 50:
   → Investigar más (entrevistas, landing page)

4. Si scoring < 50:
   → Descartar o pivotar
```

### Workflow 3: Monitoreo de Portafolio (Trimestral)

```
1. /business-analyst evaluate recochapp
2. /business-analyst evaluate ml-studios
3. /business-analyst portfolio

→ Ajustar estrategia según resultados
→ Identificar proyectos a pausar/acelerar
```

---

## 📈 Ejemplos Reales

### Ejemplo 1: Análisis Completo

**Input:**
```
Analiza la oportunidad de crear un servicio de AI audio mastering
para competir con LANDR en Estados Unidos
```

**Output:**
```markdown
# Análisis: AI Audio Mastering Service (USA)

## 📊 Resumen Ejecutivo
AI audio mastering es un mercado establecido con jugadores como LANDR
($50M raised) y eMastered. El mercado global de mastering es $500M
con crecimiento de 15% YoY...

[Análisis completo de 2-3 páginas]

## 🎯 Scoring: 68/80 🟢

## ✅ Recomendación: PRIORIZAR
Alta oportunidad con mercado probado y espacio para diferenciación...

## 🚀 Next Steps
1. Entrevistar 10 productores sobre pain points de LANDR
2. Investigar modelos open source (Demucs, Spleeter)
3. Crear PoC con mejor modelo que LANDR
4. Landing page + test de ads ($500)
5. Validar willingness to pay
```

---

## 🔧 Configuración Avanzada

### Personalizar Criterios de Scoring

Puedes pedirle a Claude que ajuste los pesos:

```
"Analiza esta oportunidad pero dame más peso a viabilidad técnica
y menos a tamaño de mercado, ya que prefiero proyectos pequeños
pero factibles"
```

### Enfoque en Mercado Específico

```
"Solo investiga oportunidades que sean viables en Alemania,
ya que ahí voy a estar durante mi doctorado"
```

### Filtrar por Capital

```
"Dame oportunidades que pueda hacer con menos de $10k de inversión inicial"
```

---

## 💡 Tips Pro

1. **Sé específico en tu request:**
   ❌ "Dame ideas"
   ✅ "Investiga oportunidades de audio tech en USA con mercado >$100M"

2. **Usa el contexto acumulado:**
   Después de un análisis, pregunta:
   "¿Cómo se compara esto con Recochapp?"

3. **Pide formatos específicos:**
   "Dame esto en formato de pitch deck de 5 slides"
   "Genera una tabla comparativa de las top 3 ideas"

4. **Combina análisis:**
   "Combina los insights de mis últimos 3 análisis y dame
   una recomendación estratégica para Q2 2026"

---

## 🆘 Troubleshooting

**Q: ¿La skill genera archivos automáticamente?**
A: Sí, cuando usas `opportunity`, crea archivos en `/docs/oportunidades-negocio/`

**Q: ¿Puedo modificar los análisis generados?**
A: Sí, los archivos son Markdown editables. Ajusta lo que necesites.

**Q: ¿Qué tan actualizada es la info de web research?**
A: Claude busca info reciente (2026) en tiempo real.

**Q: ¿Puedo analizar proyectos que no sean Recochapp o musica projects?**
A: Sí, funciona con cualquier idea que describas.

---

## 📚 Recursos Relacionados

- [Template de Oportunidad](../../docs/oportunidades-negocio/00-template-oportunidad.md)
- [Ideas Pre-investigadas](../../docs/oportunidades-negocio/IDEAS-INICIALES.md)
- [Metodología de Investigación](../../docs/oportunidades-negocio/README.md)

---

**Última actualización:** 2026-02-14
**Versión de Skill:** 1.0
