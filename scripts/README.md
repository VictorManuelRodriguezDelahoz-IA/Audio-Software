# Scripts

## sync_notion.py

Sincroniza documentación desde Notion a GitHub.

### Setup

```bash
# 1. Crear integración en Notion
# https://www.notion.so/my-integrations

# 2. Compartir páginas con la integración

# 3. Configurar
cp .env.local.example .env
# Editar .env con tu NOTION_TOKEN

# 4. Instalar y ejecutar
pip install notion-client python-dotenv
python scripts/sync_notion.py
```

### Variables de entorno

| Variable | Descripción |
|----------|-------------|
| `NOTION_TOKEN` | Token de integración de Notion |
| `NOTION_PAGE_STARTUP` | Page ID de tu página "Startup" |
| `NOTION_DATABASE_RECOCHAPP` | Database ID de Recochapp (opcional) |
| `NOTION_DATABASE_ML_STUDIOS` | Database ID de ML Studios (opcional) |

### Ejecución automática

Configurado en `.github/workflows/sync-notion.yml`:
- Se ejecuta cada lunes a las 9 AM UTC
- También se puede ejecutar manualmente desde GitHub Actions
