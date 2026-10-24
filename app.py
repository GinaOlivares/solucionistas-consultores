"""Sitio corporativo de Solucionistas Consultores. Ejecutar con streamlit run app.py."""
from base64 import b64encode
from datetime import date
from html import escape
from pathlib import Path

import streamlit as st

BASE = Path(__file__).resolve().parent
SERVICES = (
    ("Gestión y estrategia", (
        "Consultoría estratégica", "Diagnóstico y fortalecimiento de la cultura organizacional",
        "Programas de Power Skills y coaching estratégico", "Liderazgo en I+D")),
    ("Análisis y modelado", (
        "Analítica de datos", "Machine Learning", "Investigación de operaciones")),
    ("Capacitación", (
        "Asesoría en Diseño de Prototipos y Pruebas", "Implementación y entrenamiento", "R, Python, COMSOL, MATLAB")),
    ("Automatización y control", (
        "Automatización de procesos",
        "Automatización integral (RF, microondas, sistemas de control y retroalimentación)",
        "Control ambiental (vacío, estabilización térmica, blindaje electromagnético)",
        "Análisis y Control de Vibraciones Estructurales", "Reducción de Ruido y Aislamiento Acústico",
        "Ensayos No Destructivos (END)")),
    ("Tecnologías avanzadas", (
        "Tecnologías cuánticas", "Desarrollo de tecnologías basadas en MEMS", "Sensores de precisión",
        "Imágenes y detección (óptica avanzada)",
        "Mediciones de alta resolución (espectroscopía e interferometría)",
        "Procesado de señales (filtrado, reducción de ruido y análisis en tiempo real)")),
)


def asset(name: str, mime: str) -> str:
    return f"data:{mime};base64,{b64encode((BASE / 'assets' / name).read_bytes()).decode()}"


def render_site() -> str:
    symbol = asset('logo.png', 'image/png')
    cards = ''.join(
        f'<article class="service service-{i}"><span class="index">0{i}</span>'
        f'<h3>{escape(title)}</h3><ul>'
        + ''.join(f'<li>{escape(item)}</li>' for item in items)
        + '</ul></article>' for i, (title, items) in enumerate(SERVICES, 1)
    )
    return f'''
    <div class="site" lang="es">
      <a class="skip-link" href="#contenido" target="_self">Saltar al contenido</a>
      <header class="site-header" id="inicio">
        <a class="brand" href="#inicio" target="_self" aria-label="Solucionistas Consultores, inicio">
          <img src="{symbol}" alt="" width="46" height="46">
          <span>Solucionistas<small>CONSULTORES</small></span>
        </a>
        <nav aria-label="Navegación principal">
          <a href="#inicio" target="_self">Inicio</a><a href="#servicios" target="_self">Servicios</a>
          <a href="#nosotros" target="_self">Nosotros</a><a href="#contacto" target="_self">Contacto</a>
        </nav>
        <a class="header-cta" href="#contacto" target="_self">Hablemos de tu proyecto <span aria-hidden="true">↗</span></a>
      </header>
      <main id="contenido">
        <section class="hero" aria-labelledby="hero-title">
          <div class="hero-copy"><p class="eyebrow">CONSULTORÍA · TECNOLOGÍA · INNOVACIÓN</p>
            <p class="slogan">Ciencia que transforma industrias</p>
            <h1 id="hero-title">Soluciones para<br>desafíos <em>complejos.</em></h1>
            <p class="intro">Integramos estrategia, análisis, tecnología y conocimiento científico para abordar retos de organizaciones y proyectos.</p>
            <div class="actions"><a class="button primary" href="#servicios" target="_self">Explorar servicios <span aria-hidden="true">↗</span></a>
            <a class="text-link" href="#contacto" target="_self">Contactar <span aria-hidden="true">→</span></a></div>
          </div>
          <div class="hero-art" aria-hidden="true"><img src="{symbol}" alt=""><span>ESTRATEGIA + CONOCIMIENTO</span></div>
          <div class="hero-bottom"><span>Solucionistas Consultores</span><a href="#servicios" target="_self">Descubre lo que podemos hacer <span aria-hidden="true">↓</span></a></div>
        </section>
        <section id="servicios" class="section" aria-labelledby="services-title">
          <div class="section-heading"><p class="eyebrow">01 / SERVICIOS</p><div><h2 id="services-title">Distintas disciplinas.<br>Una visión integral.</h2><p>Estrategia, herramientas y conocimiento técnico para los desafíos de tu proyecto.</p></div></div>
          <div class="services-grid">{cards}</div>
        </section>
        <section id="nosotros" class="section about" aria-labelledby="about-title">
          <div class="section-heading"><p class="eyebrow">02 / NOSOTROS</p><div><h2 id="about-title">Conoce a nuestra<br>dirección.</h2><p>Una conversación es el punto de partida.</p></div></div>
          <div class="people">
            <article class="person"><p class="role">DIRECCIÓN GENERAL</p><h3>Dra. Georgina Olivares</h3><p class="position">Directora General, Solucionistas consultores</p><div class="person-contact"><a href="mailto:solucionistas.ia@gmail.com">solucionistas.ia@gmail.com <span aria-hidden="true">↗</span></a></div></article>
            <article class="person"><p class="role">DIRECCIÓN DE OPERACIONES</p><h3>Mtro. René Ramón Rousset</h3><p class="position">Director de Operaciones, Solucionistas consultores</p><div class="person-contact"><a href="mailto:roussetalanizrene@gmail.com">roussetalanizrene@gmail.com <span aria-hidden="true">↗</span></a></div></article>
          </div>
        </section>
        <section id="contacto" class="contact section" aria-labelledby="contact-title">
          <p class="eyebrow">03 / CONTACTO</p><h2 id="contact-title">Conversemos sobre<br>tu próximo <em>proyecto.</em></h2>
          <div class="contact-row"><a class="contact-email" href="mailto:solucionistas.ia@gmail.com">solucionistas.ia@gmail.com <span aria-hidden="true">↗</span></a></div>
          <a class="previous" href="https://solucionistasai.shinyapps.io/servicios/" target="_blank" rel="noopener noreferrer">Sitio de servicios anterior <span aria-hidden="true">↗</span><span class="sr-only"> (abre una nueva pestaña)</span></a>
        </section>
      </main>
      <footer><a class="footer-brand" href="#inicio" target="_self">Solucionistas Consultores</a><span>© {date.today().year} Solucionistas Consultores</span><nav aria-label="Navegación al pie"><a href="#servicios" target="_self">Servicios</a><a href="#nosotros" target="_self">Nosotros</a><a href="#contacto" target="_self">Contacto</a><a href="#inicio" target="_self" aria-label="Volver al inicio">↑</a></nav></footer>
    </div>'''


def main() -> None:
    st.set_page_config(page_title="Solucionistas Consultores", page_icon=str(BASE / 'assets' / 'logo.png'), layout="wide", initial_sidebar_state="collapsed")
    css = (BASE / 'assets' / 'style.css').read_text(encoding='utf-8')
    css = css.replace('__FABRIC__', asset('black-fabric.webp', 'image/webp'))
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    st.html(render_site())


if __name__ == '__main__':
    main()
