# Market Researcher Skill

**Nombre:** market-researcher
**Descripcion:** Investiga mercados, identifica tendencias, analiza competencia y descubre oportunidades rentables combinando datos de multiples fuentes
**Uso:** `/market-researcher [comando]`

---

## Comandos Disponibles

### 1. `/market-researcher scan [sector]`
Escaneo amplio de un sector para encontrar oportunidades

**Que hace:**
- Busca en web tendencias actuales del sector
- Identifica startups con funding reciente
- Detecta gaps en el mercado
- Lista nichos con baja competencia
- Genera ranking de oportunidades

**Sectores soportados:** audio, music-tech, ai-tools, saas, hardware, gaming, wellness, creator-economy

**Ejemplo:**
```
/market-researcher scan audio
/market-researcher scan creator-economy
/market-researcher scan ai-tools
```

---

### 2. `/market-researcher deep-dive [idea]`
Analisis profundo de una oportunidad especifica

**Que hace:**
- TAM/SAM/SOM del mercado
- Analisis de competidores (top 5-10)
- Modelo de revenue con proyecciones
- Barreras de entrada
- Tech stack necesario
- Go-to-market strategy
- Timeline estimado para MVP

**Ejemplo:**
```
/market-researcher deep-dive "AI sonic branding for SMBs"
/market-researcher deep-dive "spatial audio conversion tool"
/market-researcher deep-dive "AI jingle generator for advertisers"
```

---

### 3. `/market-researcher competitors [producto]`
Mapa competitivo detallado

**Que hace:**
- Identifica competidores directos e indirectos
- Analiza pricing de cada uno
- Compara features
- Detecta debilidades explotables
- Posicionamiento recomendado

**Ejemplo:**
```
/market-researcher competitors "atmosphere ai"
/market-researcher competitors "AI mastering service"
```

---

### 4. `/market-researcher combine [idea1] + [idea2]`
Analiza la viabilidad de combinar dos ideas en un producto unico

**Que hace:**
- Evalua sinergias entre las ideas
- Identifica mercado combinado
- Analiza si ya existe un competidor combinado
- Propone feature set integrado
- Calcula ventaja competitiva del combo
- Estima effort adicional vs beneficio

**Ejemplo:**
```
/market-researcher combine "atmosphere ai" + "silence os"
/market-researcher combine "sonic branding" + "jingle generator"
/market-researcher combine "voice cloning" + "podcast tools"
```

---

### 5. `/market-researcher trends [año]`
Tendencias globales en audio + IA para un año especifico

**Que hace:**
- Top 10 tendencias del ano
- Startups que ejemplifican cada tendencia
- Funding rounds relevantes
- Predicciones de analistas
- Oportunidades que emergen de cada tendencia

**Ejemplo:**
```
/market-researcher trends 2026
/market-researcher trends 2027
```

---

### 6. `/market-researcher validate [idea]`
Validacion rapida de una idea de negocio

**Que hace:**
- Busca si alguien ya lo hace
- Evalua demanda (Google Trends, Reddit, forums)
- Estima willingness to pay
- Identifica early adopters
- Sugiere experimento de validacion (landing page, ads)
- Da veredicto: GO / INVESTIGATE / KILL

**Ejemplo:**
```
/market-researcher validate "AI sound effects for indie game devs"
/market-researcher validate "music therapy subscription for offices"
```

---

## Metodologia de Investigacion

### Fuentes de Datos

1. **Tamano de mercado:** Reports de Grand View Research, Statista, MarketsandMarkets
2. **Startups & funding:** Tracxn, Crunchbase, PitchBook
3. **Tendencias:** Google Trends, Product Hunt, Hacker News
4. **Pain points:** Reddit, Twitter/X, forums especializados
5. **Competencia:** G2, Capterra, Product Hunt, app stores
6. **Industria musical:** Billboard, Music Business Worldwide, Water & Music

### Framework de Evaluacion

| Criterio | Peso | Descripcion |
|----------|------|-------------|
| Market Size | 15% | TAM > $500M = alto potencial |
| Growth Rate | 15% | CAGR > 20% = mercado en expansion |
| Competition | 15% | Menos competidores = mejor |
| Technical Feasibility | 15% | Podemos construirlo con nuestro stack? |
| Revenue Model | 15% | SaaS/API > one-time > ads |
| Synergy | 15% | Se complementa con productos existentes? |
| Time to Market | 10% | < 3 meses MVP = ideal |

### Scoring

- **80-100:** Oportunidad excepcional - Ejecutar ya
- **60-79:** Muy prometedor - Validar y ejecutar
- **40-59:** Potencial - Necesita mas investigacion
- **0-39:** Descartable - No invertir tiempo

---

## Integracion con Proyectos Existentes

### Contexto de musica projects

Al investigar, siempre considera:
- **Productos actuales:** SilenceOS, Lumina-Sync, Atmosphere AI
- **Tech stack:** FastAPI, Librosa, Hugging Face, NumPy
- **Ventajas:** Conocimiento en audio + ML, infraestructura existente
- **Restricciones:** Bootstrap (sin funding externo), equipo pequeno

### Sinergias a Evaluar

Cada nueva idea debe evaluarse contra:
1. Puede usar la infraestructura existente?
2. Comparte target con productos actuales?
3. Se puede cross-sell con otros productos?
4. Reduce costos de adquisicion de clientes?

---

## Output: Donde se Guardan los Reportes

- Escaneos amplios: `docs/oportunidades-negocio/global/`
- Analisis por pais: `docs/oportunidades-negocio/[pais]/`
- Deep dives: `docs/oportunidades-negocio/deep-dives/`
- Mapas competitivos: `docs/oportunidades-negocio/competitors/`

---

**Creada:** 2026-02-19
**Version:** 1.0
