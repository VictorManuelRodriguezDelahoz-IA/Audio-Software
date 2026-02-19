# Arquitectura de Sincronización Notion ↔ GitHub

## 📐 Diagrama de Flujo

```
┌─────────────────────────────────────────────────────────────┐
│                         NOTION                               │
│  ┌──────────────────┐         ┌──────────────────┐          │
│  │  Recochapp Docs  │         │ musica projects Docs  │          │
│  │    (Database)    │         │    (Database)    │          │
│  └────────┬─────────┘         └────────┬─────────┘          │
│           │                            │                     │
│           │  Ideas, Roadmap activo,    │                     │
│           │  Decisiones en evolución   │                     │
└───────────┼────────────────────────────┼─────────────────────┘
            │                            │
            │  Notion API (read-only)    │
            ▼                            ▼
┌─────────────────────────────────────────────────────────────┐
│              GITHUB ACTION (Automated Sync)                  │
│                                                              │
│  Trigger: Lunes 9 AM UTC o manual                           │
│  Script: scripts/sync_notion.py                             │
│  Libs: notion-client, markdown                              │
│                                                              │
│  ┌────────────────────────────────────────────────┐         │
│  │ 1. Fetch pages from Notion databases           │         │
│  │ 2. Convert blocks to Markdown                  │         │
│  │ 3. Add metadata (sync time, page ID)           │         │
│  │ 4. Write to /docs-notion/                      │         │
│  │ 5. Commit changes (if any)                     │         │
│  └────────────────────────────────────────────────┘         │
└───────────────────────────┬─────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                      GITHUB REPOSITORY                       │
│                                                              │
│  Recochapp/                                                  │
│  ├── docs/              ← Docs estables (edita aquí)        │
│  │   ├── 01-necesidades.md                                  │
│  │   ├── 02-roadmap.md                                      │
│  │   ├── 03-modelo-negocio.md                               │
│  │   └── 04-ideas-features.md                               │
│  │                                                           │
│  └── docs-notion/       ← Sincronizado (NO editar)          │
│      ├── README.md (autogenerado)                           │
│      ├── weekly-progress.md                                 │
│      └── brainstorm-features.md                             │
│                                                              │
│  musica projects/                                                 │
│  ├── docs/              ← Docs estables (edita aquí)        │
│  │   ├── 01-necesidades.md                                  │
│  │   ├── 02-roadmap.md                                      │
│  │   ├── 03-modelo-negocio.md                               │
│  │   └── 04-ideas-adicionales.md                            │
│  │                                                           │
│  └── docs-notion/       ← Sincronizado (NO editar)          │
│      ├── README.md (autogenerado)                           │
│      ├── product-decisions.md                               │
│      └── weekly-metrics.md                                  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
            │                            │
            │                            │
            ▼                            ▼
┌──────────────────┐         ┌──────────────────┐
│   Developers     │         │   Stakeholders   │
│                  │         │                  │
│ - Leen docs/     │         │ - Leen Notion    │
│ - Editan docs/   │         │ - Editan Notion  │
│ - Leen docs-notion/│       │ - Ven updates    │
│   (read-only)    │         │   en GitHub      │
└──────────────────┘         └──────────────────┘
```

## 🔄 Tipos de Sincronización

### Unidireccional: Notion → GitHub
```
Notion (Source of Truth para docs dinámicos)
   ↓
GitHub (Mirror, read-only)
```

**Pros:**
- Simple de implementar ✅
- No hay conflictos ✅
- Clara separación de responsabilidades ✅

**Cons:**
- No puedes editar en GitHub y reflejar en Notion ❌
- Si alguien edita en GitHub, se pierde en próxima sync ❌

### Modelo Híbrido (Implementado)
```
Notion ────────────→ /docs-notion/ (read-only)
                           ↓
                      Developers leen
                           ↑
Git ←──────────────── /docs/ (read-write)
```

**Ventajas:**
- Cada tipo de doc en su lugar ideal ✅
- No hay conflictos (separados físicamente) ✅
- Flexibilidad para diferentes workflows ✅

## 📁 Convención de Contenidos

### En Notion (Planificación y Evolución)
| Tipo de Doc | Ejemplo | Frecuencia de cambio |
|-------------|---------|----------------------|
| Weekly Progress | "Semana del 10-16 Feb" | Semanal |
| Active Roadmap | "Q1 2026 Roadmap" | Diaria/Semanal |
| Brainstorming | "Ideas para gamificación" | Continua |
| Metrics Dashboard | "KPIs Febrero 2026" | Diaria |
| Meeting Notes | "Sync Team 14 Feb" | Cada reunión |
| Decisions in Review | "¿Qué stack usar?" | Hasta decidir |

### En GitHub /docs/ (Técnico y Estable)
| Tipo de Doc | Ejemplo | Frecuencia de cambio |
|-------------|---------|----------------------|
| Architecture | "Arquitectura del sistema" | Mensual/Trimestral |
| API Docs | "Endpoints de la API" | Al agregar features |
| Setup Guides | "Cómo instalar el proyecto" | Rara vez |
| ADRs | "Por qué elegimos FastAPI" | Una vez (immutable) |
| Finalized Roadmap | "Roadmap Año 1 (cerrado)" | Una vez |

## 🛠️ Cómo Funciona el Script

### 1. Autenticación
```python
client = Client(auth=NOTION_TOKEN)
```

### 2. Query de Database
```python
results = client.databases.query(database_id=database_id)
pages = results.get('results', [])
```

### 3. Por cada página
```python
# Obtener bloques
blocks = client.blocks.children.list(page_id)

# Convertir a Markdown
markdown = blocks_to_markdown(blocks['results'])

# Agregar metadata
content = f"""---
title: {title}
synced_from_notion: true
last_sync: {datetime.now().isoformat()}
---

{markdown}
"""

# Guardar archivo
file_path.write_text(content)
```

### 4. Commit automático
```bash
git add docs-notion/
git commit -m "docs: sync from Notion [automated]"
git push
```

## 🔐 Seguridad

### Secrets en GitHub
```
NOTION_TOKEN              → Token de integración
NOTION_DATABASE_RECOCHAPP → ID de database Recochapp
NOTION_DATABASE_ML_STUDIOS → ID de database musica projects
```

### .env Local (desarrollo)
```bash
# .env (gitignored)
NOTION_TOKEN=secret_xxx
NOTION_DATABASE_RECOCHAPP=xxx
NOTION_DATABASE_ML_STUDIOS=xxx
```

## 🚨 Prevención de Conflictos

### Regla de Oro
```
┌────────────────────────────────────────┐
│  NUNCA edites archivos que tienen:    │
│                                        │
│  ---                                   │
│  synced_from_notion: true              │
│  ---                                   │
│                                        │
│  Tus cambios serán SOBRESCRITOS        │
└────────────────────────────────────────┘
```

### Validación Pre-Commit (Futuro)
```bash
# .git/hooks/pre-commit
#!/bin/bash
# Prevenir commits a docs-notion/

if git diff --cached --name-only | grep -q "docs-notion/"; then
  echo "❌ Error: No puedes editar docs-notion/"
  echo "Edita en Notion y espera la sincronización"
  exit 1
fi
```

## 📊 Monitoring

### GitHub Actions Dashboard
```
Actions → Sync Notion Docs

Recent runs:
✅ Feb 12, 2026 - Success (2 files changed)
✅ Feb 05, 2026 - Success (0 files changed)
✅ Jan 29, 2026 - Success (5 files changed)
```

### Logs de Sincronización
```
🚀 Iniciando sincronización de Notion...

📥 Sincronizando Recochapp...
  ✅ weekly-progress-feb-12.md
  ✅ brainstorm-ranking-system.md
✅ Recochapp sincronizado correctamente

📥 Sincronizando musica projects...
  ✅ product-decisions-q1.md
  ✅ metrics-february.md
  ⚠️  untitled.md (sin contenido)
✅ musica projects sincronizado correctamente

✨ Sincronización completada!
```

## 🔮 Mejoras Futuras

### 1. Sincronización Bidireccional
```python
# Detectar cambios en GitHub
# Si archivo modificado en GitHub y no tiene synced_from_notion: true
#   → Actualizar Notion
```

### 2. Conflict Resolution
```python
# Si ambos lados cambiaron:
#   1. Crear versión de conflicto
#   2. Notificar a usuario
#   3. Permitir merge manual
```

### 3. Soporte de Imágenes
```python
# Descargar imágenes de Notion
# Subir a GitHub /assets/
# Actualizar referencias en Markdown
```

### 4. Webhooks de Notion
```python
# En lugar de polling (cron), usar webhooks
# Sync inmediato cuando cambia algo en Notion
```

### 5. Notion Backlinks
```python
# Agregar link al archivo en GitHub
# Agregar link a página de Notion
# Mantener trazabilidad
```

## 🎯 Best Practices

### ✅ DO
- Edita en Notion para docs estratégicos/dinámicos
- Edita en Git para docs técnicos/estables
- Lee la metadata de archivos antes de editar
- Usa la sincronización manual para testing

### ❌ DON'T
- No edites archivos en /docs-notion/
- No mezcles docs técnicos en Notion database
- No confíes en sincronización instant (es async)
- No uses esto para código (solo docs)

## 🆘 Troubleshooting

### Problema: Sincronización no detecta cambios

**Causa:** Cache de Notion o permisos
```bash
# Verificar permisos
python -c "
from notion_client import Client
client = Client(auth='$NOTION_TOKEN')
print(client.databases.retrieve('$DATABASE_ID'))
"
```

### Problema: Formato Markdown incorrecto

**Causa:** Bloques no soportados
```python
# Ver qué bloques tienes
blocks = client.blocks.children.list(page_id)
for block in blocks['results']:
    print(block['type'])

# Agregar soporte en sync_notion.py
```

### Problema: "Changes detected" pero no hay cambios visibles

**Causa:** Whitespace o metadata changes
```bash
git diff docs-notion/
# Ver exactamente qué cambió
```

## 📚 Referencias

- [Notion API Docs](https://developers.notion.com/)
- [notion-client Python](https://github.com/ramnes/notion-sdk-py)
- [GitHub Actions](https://docs.github.com/en/actions)
