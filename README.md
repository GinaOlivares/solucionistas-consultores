# Solucionistas Consultores

Sitio corporativo en español desarrollado en Python y Streamlit. Diseño monocromático responsive, catálogo completo de servicios, dirección y contacto mediante enlaces reales de correo electrónico. No requiere claves, cuentas de terceros ni base de datos.

## Ejecución local

Requiere Python 3.11 o posterior (recomendado: 3.11).

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

En Windows, activa el entorno con `.venv\Scripts\activate`. Abre la dirección que imprime Streamlit, normalmente `http://localhost:8501`.

## GitHub

Crea un repositorio vacío en GitHub, sin inicializar README. Desde esta carpeta:

```bash
git add app.py assets .streamlit/config.toml requirements.txt README.md .gitignore tests .github
git commit -m "Implementa sitio corporativo de Solucionistas Consultores"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/solucionistas-consultores.git
git push -u origin main
```

Sustituye `TU_USUARIO` por tu usuario. Si `origin` ya existe, revisa `git remote -v` antes de modificarlo. Los documentos originales pueden permanecer locales; no son necesarios en producción. No subas `.venv`, credenciales ni archivos de `tmp`.

## Streamlit Community Cloud

1. Accede a [Streamlit Community Cloud](https://share.streamlit.io/) y conecta GitHub.
2. Selecciona **Create app**, el repositorio y la rama `main`.
3. Usa **Main file path: `app.py`**.
4. En las opciones avanzadas selecciona Python **3.11**.
5. Pulsa **Deploy**. No es necesario configurar secretos.

La plataforma instala `requirements.txt` y utiliza `.streamlit/config.toml`. Las imágenes y el CSS se incluyen en el repositorio; no dependen de fuentes ni servidores de imágenes externos.

## Estructura

- `app.py`: contenido, HTML escapado, configuración y punto de entrada.
- `assets/style.css`: diseño, adaptación móvil, foco visible y reducción de movimiento.
- `assets/symbol.png`: símbolo original aislado para encabezado, hero e icono.
- `assets/logo.png`: logotipo proporcionado por la usuaria, con transparencia; utilizado en la marca, hero e icono.
- `assets/black-fabric.webp`: textura extraída del PDF y optimizada para web.
- `.streamlit/config.toml`: tema oscuro y configuración.
- `tests/test_app.py`: ejecución Streamlit, catálogo y enlaces internos/contactos.
- `.github/workflows/check.yml`: verificación automática con GitHub Actions.

## Identidad y decisiones editoriales

`Cards.pdf` es la fuente de identidad, nombres, cargos, contactos y servicios. Se revisaron las cuatro páginas. El símbolo se extrajo de la imagen RGBA `X7.png` de la página 4, recortando únicamente el símbolo, sin recrearlo ni usar la tarjeta completa como logotipo. La textura procede del recurso fotográfico `X4.jpg`; se aplica oscurecida para conservar la legibilidad. El nombre se compone como texto accesible.

Se conservaron los cinco grupos y sus 22 servicios según el documento de especificaciones, coincidentes con la página 3 del PDF (se normalizó el espacio después de la coma en `Python, COMSOL`). Los textos de presentación son editoriales y no añaden capacidades. No se inventan clientes, cifras, ubicaciones ni biografías.

El contacto general es `solucionistas.ia@gmail.com`, mediante un enlace `mailto:` que abre la aplicación de correo configurada en el dispositivo. Por solicitud de la usuaria, se retiraron todos los números telefónicos del sitio. No se simula un formulario ni se requiere backend. El enlace al sitio anterior está identificado como tal; su disponibilidad depende de su proveedor. Las anclas usan el mismo documento y `target="_self"`.

## Verificación

```bash
python -m unittest discover -s tests -v
```

Los tests ejecutan la aplicación con `streamlit.testing.v1.AppTest`, comprueban la presencia de los 22 servicios, las anclas y los contactos. Para revisar visualmente, abre la app y comprueba también un viewport móvil de 390 px y uno de escritorio de 1440 px. La implementación adapta la navegación, los servicios y los perfiles a una columna en pantallas pequeñas.

Documentación de despliegue: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app/deploy

### Resultado de la revisión local

- Las tres pruebas automatizadas pasan.
- El servidor `streamlit run app.py` inicia correctamente.
- Se revisó la composición en navegador a 1440 px y los servicios/contacto a 390 px, con navegación a las secciones y sin desbordamiento horizontal.
- El contenido se inserta con `st.html` (sin iframe) para preservar etiquetas semánticas y anclas. El CSS local se aplica mediante `st.markdown`.
- El proyecto queda preparado en esta carpeta; todavía no se ha subido a GitHub ni publicado en Community Cloud.

Actualización de identidad: se utiliza el archivo `logo.png` suministrado posteriormente por la usuaria. En la página se aplica un filtro CSS de silueta blanca para eliminar el contorno gris y mantener su transparencia, sin marco ni sombra. Se incorpora el eslogan «Ciencia que transforma industrias» en el hero.
