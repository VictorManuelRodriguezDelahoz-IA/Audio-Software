#!/usr/bin/env python3
"""
Script para sincronizar documentación desde Notion a GitHub.

Configuración:
1. Crear integración en Notion: https://www.notion.so/my-integrations
2. Compartir las páginas con la integración
3. Configurar secrets en GitHub:
   - NOTION_TOKEN: Token de integración
   - NOTION_DATABASE_RECOCHAPP: ID de la database de Recochapp
   - NOTION_DATABASE_ML_STUDIOS: ID de la database de ML Studios
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List

try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass  # En GitHub Actions no necesita dotenv

try:
    from notion_client import Client
except ImportError:
    print("❌ Error: notion-client no instalado")
    print("Ejecuta: pip install notion-client")
    sys.exit(1)


class NotionSyncer:
    def __init__(self):
        self.notion_token = os.getenv('NOTION_TOKEN')
        if not self.notion_token:
            print("❌ Error: NOTION_TOKEN no configurado")
            sys.exit(1)

        self.client = Client(auth=self.notion_token)
        self.base_path = Path(__file__).parent.parent

    def get_page_content(self, page_id: str) -> str:
        """Obtiene el contenido de una página de Notion en markdown."""
        try:
            # Obtener bloques de la página
            blocks = self.client.blocks.children.list(page_id)
            return self._blocks_to_markdown(blocks['results'])
        except Exception as e:
            print(f"❌ Error obteniendo página {page_id}: {e}")
            return ""

    def _blocks_to_markdown(self, blocks: List[Dict]) -> str:
        """Convierte bloques de Notion a markdown."""
        markdown = []

        for block in blocks:
            block_type = block['type']

            if block_type == 'paragraph':
                text = self._extract_text(block['paragraph'])
                markdown.append(text + "\n")

            elif block_type == 'heading_1':
                text = self._extract_text(block['heading_1'])
                markdown.append(f"# {text}\n")

            elif block_type == 'heading_2':
                text = self._extract_text(block['heading_2'])
                markdown.append(f"## {text}\n")

            elif block_type == 'heading_3':
                text = self._extract_text(block['heading_3'])
                markdown.append(f"### {text}\n")

            elif block_type == 'bulleted_list_item':
                text = self._extract_text(block['bulleted_list_item'])
                markdown.append(f"- {text}\n")

            elif block_type == 'numbered_list_item':
                text = self._extract_text(block['numbered_list_item'])
                markdown.append(f"1. {text}\n")

            elif block_type == 'to_do':
                text = self._extract_text(block['to_do'])
                checked = "x" if block['to_do'].get('checked') else " "
                markdown.append(f"- [{checked}] {text}\n")

            elif block_type == 'code':
                text = self._extract_text(block['code'])
                language = block['code'].get('language', '')
                markdown.append(f"```{language}\n{text}\n```\n")

            elif block_type == 'quote':
                text = self._extract_text(block['quote'])
                markdown.append(f"> {text}\n")

            elif block_type == 'divider':
                markdown.append("---\n")

        return "\n".join(markdown)

    def _extract_text(self, block_content: Dict) -> str:
        """Extrae texto de un bloque con formato."""
        if 'rich_text' not in block_content:
            return ""

        text_parts = []
        for text_obj in block_content['rich_text']:
            text = text_obj.get('plain_text', '')

            # Aplicar formato markdown
            if text_obj.get('annotations', {}).get('bold'):
                text = f"**{text}**"
            if text_obj.get('annotations', {}).get('italic'):
                text = f"*{text}*"
            if text_obj.get('annotations', {}).get('code'):
                text = f"`{text}`"
            if text_obj.get('annotations', {}).get('strikethrough'):
                text = f"~~{text}~~"

            # Enlaces
            if text_obj.get('href'):
                text = f"[{text}]({text_obj['href']})"

            text_parts.append(text)

        return "".join(text_parts)

    def sync_database(self, database_id: str, output_dir: Path, project_name: str):
        """Sincroniza una database de Notion a una carpeta del repo."""
        print(f"\n📥 Sincronizando {project_name}...")

        try:
            # Consultar database
            results = self.client.databases.query(database_id=database_id)
            pages = results.get('results', [])

            if not pages:
                print(f"⚠️  No se encontraron páginas en la database de {project_name}")
                return

            # Crear carpeta si no existe
            notion_dir = output_dir / "docs-notion"
            notion_dir.mkdir(exist_ok=True, parents=True)

            # Sincronizar cada página
            for page in pages:
                page_id = page['id']

                # Obtener título de la página
                title_prop = page['properties'].get('Name', {}) or page['properties'].get('Título', {})
                if title_prop.get('title'):
                    title = title_prop['title'][0]['plain_text']
                else:
                    title = "Untitled"

                # Sanitizar nombre de archivo
                filename = self._sanitize_filename(title) + ".md"

                # Obtener contenido
                content = self.get_page_content(page_id)

                if content:
                    # Agregar metadata
                    metadata = f"""---
title: {title}
synced_from_notion: true
last_sync: {datetime.now().isoformat()}
notion_page_id: {page_id}
---

"""
                    full_content = metadata + content

                    # Guardar archivo
                    file_path = notion_dir / filename
                    file_path.write_text(full_content, encoding='utf-8')
                    print(f"  ✅ {filename}")
                else:
                    print(f"  ⚠️  {filename} (sin contenido)")

            # Crear README en docs-notion
            readme_path = notion_dir / "README.md"
            readme_content = f"""# Documentación sincronizada desde Notion

**Proyecto:** {project_name}
**Última sincronización:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

⚠️ **IMPORTANTE:** Estos archivos son sincronizados automáticamente desde Notion.
No edites directamente aquí. Edita en Notion y la sincronización se hará automáticamente.

## Páginas sincronizadas

"""
            for md_file in sorted(notion_dir.glob("*.md")):
                if md_file.name != "README.md":
                    readme_content += f"- [{md_file.stem}]({md_file.name})\n"

            readme_path.write_text(readme_content, encoding='utf-8')

            print(f"✅ {project_name} sincronizado correctamente")

        except Exception as e:
            print(f"❌ Error sincronizando {project_name}: {e}")

    def _sanitize_filename(self, title: str) -> str:
        """Convierte título a nombre de archivo válido."""
        # Remover caracteres no válidos
        invalid_chars = '<>:"/\\|?*'
        for char in invalid_chars:
            title = title.replace(char, '')

        # Reemplazar espacios por guiones
        title = title.strip().replace(' ', '-').lower()

        # Limitar longitud
        return title[:50]

    def sync_page_to_docs(self, page_id: str, output_dir: Path, project_name: str):
        """Sincroniza una página de Notion (no database) a una carpeta del repo."""
        print(f"\n📥 Sincronizando {project_name} (página)...")

        try:
            # Obtener información de la página
            page = self.client.pages.retrieve(page_id)

            # Obtener contenido
            content = self.get_page_content(page_id)

            if content:
                # Crear carpeta si no existe
                output_dir.mkdir(exist_ok=True, parents=True)

                # Agregar metadata
                metadata = f"""---
title: {project_name}
synced_from_notion: true
last_sync: {datetime.now().isoformat()}
notion_page_id: {page_id}
---

"""
                full_content = metadata + content

                # Guardar archivo principal
                file_path = output_dir / "STARTUP-HQ.md"
                file_path.write_text(full_content, encoding='utf-8')
                print(f"  ✅ STARTUP-HQ.md")

                # Crear README
                readme_path = output_dir / "README.md"
                readme_content = f"""# Startup HQ - Sincronizado desde Notion

**Última sincronización:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

⚠️ **IMPORTANTE:** Estos archivos son sincronizados automáticamente desde Notion.
No edites directamente aquí. Edita en Notion y la sincronización se hará automáticamente.

## Documentos

- [STARTUP-HQ.md](STARTUP-HQ.md) - Documento principal del HQ
- [Ver en Notion](https://notion.so/{page_id.replace('-', '')})

---

Para editar, ve a Notion y actualiza la página "Startup".
La sincronización ocurre automáticamente los lunes a las 9 AM o manualmente desde GitHub Actions.
"""
                readme_path.write_text(readme_content, encoding='utf-8')

                print(f"✅ {project_name} sincronizado correctamente")
            else:
                print(f"  ⚠️  {project_name} (sin contenido)")

        except Exception as e:
            print(f"❌ Error sincronizando {project_name}: {e}")

    def run(self):
        """Ejecuta la sincronización completa."""
        print("🚀 Iniciando sincronización de Notion...")

        # Startup HQ (página principal)
        startup_page = os.getenv('NOTION_PAGE_STARTUP')
        if startup_page:
            self.sync_page_to_docs(
                startup_page,
                self.base_path / "docs" / "startup-hq",
                "Startup HQ"
            )
        else:
            print("⚠️  NOTION_PAGE_STARTUP no configurado, saltando...")

        # Recochapp
        recochapp_db = os.getenv('NOTION_DATABASE_RECOCHAPP')
        if recochapp_db:
            self.sync_database(
                recochapp_db,
                self.base_path / "Recochapp",
                "Recochapp"
            )
        else:
            print("⚠️  NOTION_DATABASE_RECOCHAPP no configurado, saltando...")

        # ML Studios
        ml_studios_db = os.getenv('NOTION_DATABASE_ML_STUDIOS')
        if ml_studios_db:
            self.sync_database(
                ml_studios_db,
                self.base_path / "ML Studios",
                "ML Studios"
            )
        else:
            print("⚠️  NOTION_DATABASE_ML_STUDIOS no configurado, saltando...")

        print("\n✨ Sincronización completada!")


if __name__ == "__main__":
    syncer = NotionSyncer()
    syncer.run()
