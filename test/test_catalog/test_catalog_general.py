# coding: utf-8


import re

from test.test_catalog import TestCatalogBase


class TestCatalogGeneral(TestCatalogBase):

    def test_about(self):
        about_text = self.catalog.about()

    def test_gsversion(self):
        gsversion = self.catalog.gsversion()
        pat = re.compile('\d\.\d{1,2}(\.[\dx]|-SNAPSHOT)')
        self.assertTrue(pat.match(gsversion))

    def test_reload(self):
        r = self.catalog.reload()
        self.assertEqual(r.status_code, 200)

    def test_reset(self):
        r = self.catalog.reset()
        self.assertEqual(r.status_code, 200)
