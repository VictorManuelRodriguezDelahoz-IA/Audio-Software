# ✅ Checklist de Configuración de Notion

## 🎯 Tu Situación Actual

**Página de Notion:** https://www.notion.so/Startup-2ff43c54da3d8015a5ebf7992d0ceaff
**Page ID:** `2ff43c54-da3d-8015-a5eb-f7992d0ceaff`

### ✅ Lo que YA está configurado:
- ✅ Script de sincronización creado
- ✅ Tu Page ID ya está pre-configurado en `.env.local.example`
- ✅ GitHub Action configurado
- ✅ Documentación completa

### ⏳ Lo que FALTA hacer (SOLO 3 pasos):

---

## Paso 1: Crear Integración en Notion (2 minutos)

### 1.1 Ve a My Integrations
🔗 **Abre:** https://www.notion.so/my-integrations

### 1.2 Crea nueva integración
1. Click en **"+ New integration"** (botón azul)
2. Llena el formulario:
   ```
   Name: GitHub Docs Sync
   Associated workspace: [Selecciona tu workspace]
   Type: Internal Integration
   Capabilities:
     ✅ Read content
     ✅ Read comments (opcional)
   ```
3. Click **"Submit"**

### 1.3 Copia el Token
Verás algo como:
```
┌─────────────────────────────────────────────┐
│ Internal Integration Token                  │
│                                             │
│ secret_a1b2c3d4e5f6...                     │ ← ESTE ES TU TOKEN
│                                             │
│ [👁 Show] [📋 Copy]                         │
└─────────────────────────────────────────────┘
```

📝 **IMPORTANTE:** Copia este token y guárdalo temporalmente (lo usarás en Paso 3)

---

## Paso 2: Compartir tu Página "Startup" con la Integración (1 minuto)

### 2.1 Abre tu página
🔗 **Abre:** https://www.notion.so/Startup-2ff43c54da3d8015a5ebf7992d0ceaff

### 2.2 Comparte con la integración
1. **Click en "..." (esquina superior derecha)**
2. **Selecciona "Add connections"** (o "Connections" si ya ves esa opción)
3. **Busca "GitHub Docs Sync"** (la integración que acabas de crear)
4. **Click en ella para seleccionarla**
5. **Click "Confirm"**

### 2.3 Verifica
Deberías ver un pequeño ícono de conexión en tu página:
```
Startup  🔗 GitHub Docs Sync
```

---

## Paso 3: Configurar Localmente (2 minutos)

### 3.1 Copia el archivo de ejemplo
```bash
cd /workspaces/Audio-Software
cp .env.local.example .env
```

### 3.2 Edita el archivo .env
Abre `.env` y reemplaza SOLO el token:

**ANTES:**
```bash
NOTION_TOKEN=secret_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
NOTION_PAGE_STARTUP=2ff43c54-da3d-8015-a5eb-f7992d0ceaff  # ← Ya está configurado
```

**DESPUÉS:**
```bash
NOTION_TOKEN=secret_TU_TOKEN_REAL_AQUI  # ← Pega el token del Paso 1.3
NOTION_PAGE_STARTUP=2ff43c54-da3d-8015-a5eb-f7992d0ceaff  # ← Ya está configurado, NO cambiar
```

### 3.3 Instala dependencias
```bash
pip install notion-client python-dotenv
```

### 3.4 Ejecuta la primera sincronización
```bash
python scripts/sync_notion.py
```

**Deberías ver:**
```
🚀 Iniciando sincronización de Notion...

📥 Sincronizando Startup HQ (página)...
  ✅ STARTUP-HQ.md
✅ Startup HQ sincronizado correctamente

⚠️  NOTION_DATABASE_RECOCHAPP no configurado, saltando...
⚠️  NOTION_DATABASE_ML_STUDIOS no configurado, saltando...

✨ Sincronización completada!
```

### 3.5 Verifica el resultado
```bash
cat docs/startup-hq/STARTUP-HQ.md
```

Deberías ver el contenido de tu página de Notion en Markdown.

---

## ❌ Problemas Comunes

### Error: "Unauthorized" o "object not found"
**Causa:** No compartiste la página con la integración
**Solución:** Repite Paso 2 asegurándote de hacer "Add connections"

### Error: "NOTION_TOKEN not found"
**Causa:** El archivo .env no existe o está mal configurado
**Solución:**
```bash
ls -la .env  # Verificar que existe
cat .env     # Verificar que tiene el token
```

### La sincronización no trae contenido
**Causa:** Tu página "Startup" en Notion está vacía
**Solución:** Agrega algo de contenido en Notion y vuelve a sincronizar

---

## ✅ Una Vez Funcionando Localmente

### Opcional: Configurar GitHub Actions (para sync automático)

1. Ve a tu repo en GitHub
2. Settings → Secrets and variables → Actions
3. New repository secret:
   ```
   Name: NOTION_TOKEN
   Value: [Tu token de Paso 1.3]
   ```
4. New repository secret:
   ```
   Name: NOTION_PAGE_STARTUP
   Value: 2ff43c54-da3d-8015-a5eb-f7992d0ceaff
   ```

Ahora cada lunes a las 9 AM sincronizará automáticamente.

---

## 🎯 Resumen Visual

```
┌────────────────────────────────────────────────┐
│ PASO 1: Crear integración en Notion           │
│ https://www.notion.so/my-integrations         │
│ → Copiar token                                 │
└────────────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────────────┐
│ PASO 2: Compartir página con integración      │
│ https://www.notion.so/Startup-2ff...           │
│ → "..." → Add connections → GitHub Docs Sync  │
└────────────────────────────────────────────────┘
              ↓
┌────────────────────────────────────────────────┐
│ PASO 3: Configurar localmente                 │
│ cp .env.local.example .env                     │
│ → Editar .env con tu token                     │
│ → python scripts/sync_notion.py                │
└────────────────────────────────────────────────┘
```

---

## 🆘 ¿Necesitas Ayuda?

Si tienes problemas en cualquier paso, avísame y te guío específicamente.

---

**Última actualización:** 2026-02-14
