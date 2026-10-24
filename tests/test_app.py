"""Pruebas de renderizado real y contrato de navegación del sitio."""
import unittest
from html.parser import HTMLParser
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from app import render_site, SERVICES
from streamlit.testing.v1 import AppTest


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs:
            self.ids.add(attrs['id'])
        if tag == 'a':
            self.links.append(attrs.get('href', ''))


class SiteTest(unittest.TestCase):
    def test_app_starts_and_renders(self):
        app = AppTest.from_file(str(Path(__file__).resolve().parents[1] / 'app.py')).run(timeout=30)
        self.assertFalse(app.exception)
        self.assertTrue(any('Conversemos sobre' in block.proto.body for block in app.get('html')))

    def test_navigation_and_contact(self):
        page = Links()
        page.feed(render_site())
        self.assertNotIn("tel:", render_site())
        for link in page.links:
            if link.startswith('#'):
                self.assertIn(link[1:], page.ids)
        for link in ('mailto:solucionistas.ia@gmail.com', 'mailto:roussetalanizrene@gmail.com',
                     'https://solucionistasai.shinyapps.io/servicios/'):
            self.assertIn(link, page.links)

    def test_complete_service_catalog(self):
        self.assertEqual([len(items) for _, items in SERVICES], [4, 3, 3, 6, 6])
        page = render_site()
        for title, items in SERVICES:
            self.assertIn(title, page)
            for item in items:
                self.assertIn(item, page)


if __name__ == '__main__':
    unittest.main()
