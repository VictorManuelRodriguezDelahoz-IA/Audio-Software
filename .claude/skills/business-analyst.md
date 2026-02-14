# Business Analyst Skill 📊

**Nombre:** business-analyst
**Descripción:** Analiza negocios, evalúa oportunidades y genera reportes de investigación
**Uso:** `/business-analyst [comando]`

---

## Comandos Disponibles

### 1. `/business-analyst evaluate [proyecto]`
Evalúa un proyecto existente (Recochapp, ML Studios, etc.)

**Qué hace:**
- Lee la documentación del proyecto
- Analiza modelo de negocio
- Evalúa viabilidad
- Genera scoring
- Identifica riesgos y oportunidades

**Ejemplo:**
```
/business-analyst evaluate recochapp
/business-analyst evaluate ml-studios
```

---

### 2. `/business-analyst research [mercado] [sector]`
Investiga oportunidades en un mercado y sector específico

**Mercados:** colombia, usa, alemania, global
**Sectores:** audio, tech, hardware, all

**Qué hace:**
- Busca tendencias en la web (2026)
- Analiza tamaño de mercado
- Identifica competencia
- Encuentra startups recientes con funding
- Detecta pain points

**Ejemplo:**
```
/business-analyst research usa audio
/business-analyst research alemania tech
/business-analyst research colombia all
```

---

### 3. `/business-analyst opportunity [nombre-idea]`
Investiga una oportunidad específica y genera análisis completo

**Qué hace:**
- Crea archivo de análisis usando el template
- Investiga mercado en la web
- Scoring automático (0-80)
- Recomendación (priorizar/investigar/descartar)

**Ejemplo:**
```
/business-analyst opportunity "AI Audio Mastering"
/business-analyst opportunity "Audio para Retail Colombia"
```

---

### 4. `/business-analyst compare [proyecto1] vs [proyecto2]`
Compara dos proyectos o ideas

**Qué hace:**
- Análisis comparativo
- Pros/cons de cada uno
- Scoring lado a lado
- Recomendación de priorización

**Ejemplo:**
```
/business-analyst compare recochapp vs ml-studios
/business-analyst compare "AI Mastering" vs "Voice Cloning"
```

---

### 5. `/business-analyst portfolio`
Analiza el portafolio completo de proyectos

**Qué hace:**
- Overview de todos los proyectos
- Diversificación de riesgo
- Proyecciones combinadas
- Gaps y oportunidades
- Recomendaciones estratégicas

**Ejemplo:**
```
/business-analyst portfolio
```

---

### 6. `/business-analyst trends [sector] [año]`
Investiga tendencias de un sector para un año específico

**Qué hace:**
- Web search de tendencias
- Reportes de industria
- Startups emergentes
- Tecnologías disruptivas
- Predicciones de expertos

**Ejemplo:**
```
/business-analyst trends audio 2026
/business-analyst trends ai 2027
```

---

## Metodología de Análisis

### Scoring System (0-80 puntos)

Cada oportunidad se evalúa en 8 dimensiones:

| Dimensión | Peso | Qué evalúa |
|-----------|------|------------|
| Tamaño de Mercado | 10 | TAM, SAM, SOM, crecimiento |
| Innovación | 10 | Qué tan novedoso es |
| Ventaja Competitiva | 10 | Defensibilidad, moats |
| Viabilidad Técnica | 10 | Complejidad, recursos necesarios |
| Alineación Personal | 10 | Fit con skills y pasiones |
| Potencial de Impacto | 10 | Problema que resuelve |
| Time to Market | 10 | Qué tan rápido se puede lanzar |
| Capital Requerido | 10 | Inversión necesaria |

**Interpretación:**
- **65-80:** 🟢 Excepcional - Priorizar
- **50-64:** 🟡 Prometedor - Investigar más
- **35-49:** 🟠 Potencial limitado - Revisar en 6 meses
- **0-34:** 🔴 No viable - Descartar

### Web Research Strategy

Al investigar, busca:
1. **Tamaño de mercado:** "[sector] market size [country] 2026"
2. **Tendencias:** "[sector] trends 2026", "[sector] growth rate"
3. **Competencia:** "top [sector] startups", "Y Combinator [sector]"
4. **Funding:** "recent [sector] funding rounds", "[sector] unicorns"
5. **Pain points:** Reddit r/[sector], "[industry] challenges 2026"

### Output Format

Todos los análisis generan:
1. **Resumen ejecutivo** (2-3 párrafos)
2. **Scoring detallado** (tabla con puntajes)
3. **SWOT analysis** (Fortalezas, Debilidades, Oportunidades, Amenazas)
4. **Recomendación** (Priorizar/Investigar/Descartar)
5. **Next Steps** (Acciones concretas)

---

## Ejemplos de Uso Completos

### Ejemplo 1: Evaluar Proyecto Existente

**Comando:**
```
/business-analyst evaluate recochapp
```

**Output Esperado:**
```markdown
# Análisis de Recochapp - Plataforma de Fútbol Casual

## 📊 Resumen Ejecutivo
Recochapp es una plataforma para conectar jugadores de fútbol casual...
[Análisis detallado]

## 🎯 Scoring (0-80)
| Dimensión | Puntaje | Justificación |
|-----------|---------|---------------|
| Tamaño de Mercado | 7/10 | Mercado local pero grande... |
...
**TOTAL: 58/80** 🟡

## 💪 SWOT Analysis
**Fortalezas:**
- Conocimiento local del mercado
- Enfoque en nicho específico

**Debilidades:**
- Dependencia de masa crítica...

## ✅ Recomendación: INVESTIGAR MÁS
Proyecto prometedor con potencial...

## 🚀 Next Steps
1. Validar con 10 entrevistas a jugadores
2. Crear landing page MVP
3. Test de anuncios ($200)
```

---

### Ejemplo 2: Investigar Oportunidad Nueva

**Comando:**
```
/business-analyst research usa audio
```

**Output Esperado:**
```markdown
# Investigación: Oportunidades en Audio (USA)

## 🔍 Web Research Summary
[Datos obtenidos de búsquedas web]

## 💡 Oportunidades Identificadas

### 1. AI-Powered Audio Mastering
- **Mercado:** $500M, creciendo 15% YoY
- **Competidores:** LANDR ($50M raised), eMastered
- **Pain Point:** Mastering es caro ($100-500 por canción)
...

### 2. Voice Cloning para Audiobooks
...

## 📈 Tendencias 2026
1. IA generativa en audio (explosion)
2. Creator economy creciendo
3. Podcasting madurando
...

## ✅ Top 3 Recomendaciones
1. AI Audio Mastering (Score: 68/80)
2. Podcast Production SaaS (Score: 61/80)
3. Audio Plugin Marketplace (Score: 59/80)
```

---

### Ejemplo 3: Análisis de Oportunidad Específica

**Comando:**
```
/business-analyst opportunity "AI Audio Mastering"
```

**Qué hace:**
1. Crea archivo: `docs/oportunidades-negocio/usa/01-ai-audio-mastering.md`
2. Usa el template de análisis
3. Llena automáticamente con web research
4. Calcula scoring
5. Guarda el archivo

**Output:**
```
✅ Análisis completado y guardado en:
   docs/oportunidades-negocio/usa/01-ai-audio-mastering.md

📊 Scoring: 68/80 🟢

✅ Recomendación: PRIORIZAR
Esta oportunidad tiene alto potencial...

🚀 Next Steps:
1. Entrevistar a 5 productores musicales
2. Investigar modelos open source (RVC, SoVITS)
3. Crear PoC en 2 semanas
```

---

## 🧠 Capacidades Avanzadas

### Multi-Source Research
La skill busca información en:
- Google Trends
- Crunchbase (startups y funding)
- Y Combinator library
- Product Hunt
- Reddit (pain points)
- Industry reports (Gartner, McKinsey)

### Contextual Awareness
La skill entiende:
- Tus skills (audio, tech, ML)
- Tu contexto (doctorado en Alemania)
- Tus proyectos actuales
- Tus recursos disponibles

### Smart Recommendations
Basadas en:
- Tu portafolio actual (diversificación)
- Sinergias entre proyectos
- Timing (qué hacer ahora vs después)
- Fit personal

---

## 📁 Archivos Generados

La skill puede crear/actualizar:
- `/docs/oportunidades-negocio/[país]/[nombre].md` - Análisis completo
- `/docs/startup-hq/evaluaciones/[proyecto]-eval.md` - Evaluaciones de proyectos
- `/docs/oportunidades-negocio/research-reports/[tema].md` - Reportes de research

---

## 🔧 Configuración

La skill usa:
- WebSearch para investigación
- Grep/Read para analizar docs existentes
- Write para generar reportes
- Tu contexto personal (páginas de Notion sincronizadas)

---

## 💡 Tips de Uso

1. **Empieza amplio, luego específico:**
   ```
   /business-analyst research usa audio        # Amplio
   /business-analyst opportunity "AI Mastering" # Específico
   ```

2. **Evalúa regularmente tus proyectos:**
   ```
   /business-analyst evaluate recochapp  # Cada trimestre
   ```

3. **Compara antes de decidir:**
   ```
   /business-analyst compare idea1 vs idea2
   ```

4. **Revisa tu portafolio:**
   ```
   /business-analyst portfolio  # Mensual
   ```

---

## 🎯 Casos de Uso

### Caso 1: Decidir Próximo Proyecto
```
1. /business-analyst portfolio
2. /business-analyst research [mercado prioritario] [sector]
3. /business-analyst opportunity "[top idea]"
4. /business-analyst compare "[idea nueva]" vs "[proyecto actual]"
5. Decisión informada
```

### Caso 2: Validar Idea Existente
```
1. /business-analyst opportunity "[mi idea]"
2. Revisar scoring y recomendación
3. Si >50: investigar más
4. Si <50: descartar o pivotar
```

### Caso 3: Monitoreo de Portafolio
```
Cada mes:
1. /business-analyst evaluate recochapp
2. /business-analyst evaluate ml-studios
3. /business-analyst portfolio
4. Ajustar estrategia
```

---

## 📊 KPIs que Trackea

- Proyecciones financieras (Year 1-3)
- Tamaño de mercado (TAM/SAM/SOM)
- Velocidad de crecimiento de sector
- Nivel de competencia
- Capital requerido
- Time to market
- Risk score

---

**Creada:** 2026-02-14
**Versión:** 1.0
**Mantenida por:** Sistema de análisis automatizado
