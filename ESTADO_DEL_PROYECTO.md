# Estado del Proyecto: "Audio-Software"

> Ultima actualizacion: 2026-02-19

Este documento resume el estado actual del repositorio, las decisiones tomadas y las acciones realizadas. Sirve como punto de re-entrada para retomar el trabajo.

---

## 1. Vision General y Estructura

El repositorio funciona como una "Startup HQ" que alberga multiples proyectos:

| Proyecto | Descripcion | Estado |
|----------|-------------|--------|
| **Recochapp** | App full-stack para futbol casual | Refactorizado, funcional |
| **musica projects** | Laboratorio de audio + IA (AtmoSphere) | **MVP funcional** |
| **therian-app** | App wellness para comunidad therian | Completa (sin trackear) |

Se implemento un sistema de **sincronizacion con Notion** (GitHub Action semanal) y un conjunto de **4 Claude Skills** para asistencia automatizada.

---

## 2. Estado de `Recochapp`

**Estado:** Refactorizado y funcional, listo para continuar desarrollo.

- Backend FastAPI corregido y operativo (usuarios, login, partidos)
- Frontend Next.js con pagina de inicio funcional
- Docker Compose configurado (backend + frontend + PostgreSQL)
- Variables de entorno consolidadas en `.env.example`

**Siguiente paso:** Agregar features adicionales o validar con usuarios.

---

## 3. Estado de `musica projects` (PRINCIPAL)

**Estado: MVP de AtmoSphere implementado y funcionando.**

### Que es AtmoSphere

AtmoSphere es la fusion de dos productos originales:
- **Atmosphere AI** (musica generativa royalty-free para negocios)
- **SilenceOS** (enmascaramiento acustico inteligente)

Combinados en una plataforma B2B SaaS para hoteles, restaurantes, spas, oficinas y retail.

### Endpoints operativos

| Metodo | Ruta | Descripcion |
|--------|------|-------------|
| `GET` | `/` | Health check + info del producto |
| `GET` | `/atmosphere/scenes` | 6 escenas pre-configuradas por tipo de negocio |
| `GET` | `/atmosphere/scenes/{id}` | Detalle de una escena |
| `POST` | `/atmosphere/generate` | Genera musica ambiental (por escena o custom) |
| `GET` | `/masking/profiles` | 5 perfiles de ruido disponibles |
| `POST` | `/masking/generate` | Genera audio de enmascaramiento acustico |
| `POST` | `/analyze` | Analisis de frecuencias de archivo WAV |

### Escenas de negocio implementadas

| ID | Nombre | Genero | Target |
|----|--------|--------|--------|
| `hotel-lobby` | Hotel Lobby | Ambient Jazz | Hotels & Hospitality |
| `spa-relax` | Spa & Relax | Nature Ambient | Spas, Wellness Centers |
| `restaurant-dinner` | Restaurant Dinner | Bossa Lounge | Restaurants, Wine Bars |
| `office-focus` | Office Focus | Minimal Electronic | Offices, Coworking |
| `retail-energy` | Retail Energy | Pop Instrumental | Retail, Shopping Malls |
| `cafe` | Cafe | Acoustic Chill | Cafes, Bakeries |

### Perfiles de noise masking (DSP real)

| ID | Tipo | Algoritmo | Recomendado para |
|----|------|-----------|------------------|
| `white` | White Noise | Distribucion uniforme | Concentracion general |
| `pink` | Pink Noise | Voss-McCartney 1/f | Oficinas, salas de espera |
| `brown` | Brown Noise | Random walk browniano | Spas, meditacion, dormir |
| `speech-masking` | Speech Masking | Butterworth band-pass 300-3000Hz | Call centers, oficinas abiertas |
| `office-hum` | Office Hum | Low-pass + armonicos 60/120Hz | Oficinas silenciosas |

### Arquitectura actual

```
musica projects/
├── config.py                    # Settings (pydantic-settings)
├── main.py                      # FastAPI + CORS + 3 routers
├── requirements.txt             # fastapi, uvicorn, librosa, numpy, scipy, pydantic-settings
├── api/
│   ├── atmosphere.py            # Router: /atmosphere/*
│   ├── noise_masking.py         # Router: /masking/*
│   └── sound_analysis.py        # Router: /analyze
├── schemas/
│   ├── __init__.py              # Exports de todos los schemas
│   ├── atmosphere.py            # GenerateRequest, GenerateResponse, Scene, Mood, Energy, Genre
│   └── noise_masking.py         # MaskingRequest, MaskingResponse, NoiseProfile, NoiseType
├── services/
│   ├── music_generator.py       # Sintesis DSP de musica ambiental + sistema de escenas
│   ├── noise_masking.py         # Generacion real de ruido coloreado (white/pink/brown/speech/office)
│   └── sound_processor.py       # Analisis de audio con Librosa (STFT, frecuencias)
├── utils/
│   └── file_utils.py            # Utilidades de archivos temporales
└── docs/
    ├── 01-necesidades.md        # Analisis de necesidades por producto
    ├── 02-roadmap.md            # Roadmap de implementacion a 5 anos
    ├── 03-modelo-negocio.md     # Business model canvas completo
    └── 04-ideas-adicionales.md  # Pipeline de ideas experimentales
```

### Como ejecutar

```bash
cd "musica projects"
pip install -r requirements.txt
uvicorn main:app --reload
# Abrir http://localhost:8000/docs para Swagger UI
```

### Estrategia de IA (escalonada)

1. **Fase actual (MVP):** Sintesis DSP (ondas sinusoidales + ruido coloreado). Funcional sin GPU.
2. **Siguiente paso:** Integrar MusicGen/AudioCraft de Hugging Face para generacion real de musica.
3. **Largo plazo:** Fine-tuning de modelos propios, modelo generativo propietario.

---

## 4. Investigacion de Mercado (2026-02-19)

Se realizo una investigacion exhaustiva del mercado audio + IA. Reporte completo en:
`docs/oportunidades-negocio/global/investigacion-audio-ai-2026.md`

### Cifras clave

| Segmento | Valor 2025 | CAGR |
|----------|-----------|------|
| AI en Musica | $6.65B | 27.8% |
| Audio Espacial + IA | $1.99B | ~25% |
| Voice Cloning | ~$1.1B | 37.1% |
| Sound Therapy | $1.2B | 10.2% |

### 5 ideas combinadas identificadas

1. **AtmoSphere** (en desarrollo) - Audio ambiental B2B, $99-499/mes
2. **BrandSonic** - Identidad sonora as a Service para PYMEs
3. **SoundForge AI** - All-in-one para creadores de contenido
4. **GameSound AI** - Audio generativo para game devs
5. **SampleForge** - Marketplace de samples IA

---

## 5. Claude Skills (4 disponibles)

Ubicacion: `.claude/skills/`

| Skill | Archivo | Proposito |
|-------|---------|-----------|
| **business-analyst** | `business-analyst.md` | Evaluar proyectos, investigar oportunidades, scoring |
| **code-auditor** | `code-auditor.md` | Auditoria de codigo, seguridad, arquitectura |
| **test-generator** | `test-generator.md` | Generar y ejecutar tests (pytest, Jest) |
| **market-researcher** | `market-researcher.md` | Investigar mercados, competencia, validacion |

---

## 6. Tareas Pendientes y Proximos Pasos

### Prioridad Alta

- [ ] **Integrar MusicGen/AudioCraft:** Reemplazar sintesis DSP con generacion real de musica via Hugging Face (`transformers` + `torch`)
- [ ] **Agregar tests:** Usar la skill `test-generator` para crear tests de los endpoints de AtmoSphere
- [ ] **Landing page:** Crear pagina web simple para mostrar AtmoSphere a potenciales clientes B2B

### Prioridad Media

- [ ] **Base de datos:** Agregar PostgreSQL para usuarios, suscripciones y cache de audio generado
- [ ] **Autenticacion:** JWT auth para proteger endpoints
- [ ] **Frontend dashboard:** Panel B2B para que gerentes configuren sus escenas
- [ ] **Validar con clientes:** Contactar 5-10 hoteles/restaurantes para demo

### Prioridad Baja

- [ ] **Validar Sincronizacion con Notion:** Revisar logs de GitHub Action
- [ ] **Commit de therian-app:** Esta funcional pero sin trackear en git
- [ ] **Explorar BrandSonic:** Segunda idea mas rentable segun investigacion
- [ ] **Hardware NeuroSense:** Prototipo ESP32 para captura de audio ambiente

---

## 7. Historial de Sesiones

### Sesion 2026-02-19 (HOY)

**Cambios realizados:**
1. Renombrada carpeta `ML Studios/` -> `musica projects/` (+ actualizacion de 15+ archivos de referencia)
2. Creadas 3 nuevas Claude Skills: `code-auditor`, `test-generator`, `market-researcher`
3. Investigacion de mercado audio + IA 2026 con datos reales y 5 ideas combinadas
4. **Implementado MVP de AtmoSphere:** Backend FastAPI completo con:
   - 6 escenas de negocio pre-configuradas
   - 5 perfiles de noise masking con DSP real
   - Schemas Pydantic validados
   - Generacion de audio real (WAV base64)
   - Swagger UI documentado automaticamente
5. Todos los endpoints probados y funcionando

**Commits:**
- `a0a4ce0` - feat(project): rename ML Studios, add skills and market research
- `2ba0186` - feat(atmosphere): implement AtmoSphere MVP

### Sesion anterior (2026-02-14~)

- Auditoria inicial y refactorizacion del repositorio
- Creacion de skill `business-analyst`
- Documentacion completa de roadmap, modelo de negocio y necesidades
- Organizacion de oportunidades de negocio por pais
