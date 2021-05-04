# coding: utf-8

import os
from test.test_catalog import TestCatalogBase, BASE_PATH


class TestCatalogResource(TestCatalogBase):

    def test_get_resources(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        resources = self.catalog.get_resources()
        print("Resources: {}".format(resources))

    def test_get_resource(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        resource_name = "gsconfig_test_create_imagemosaic"
        resource = self.catalog.get_resource(resource_name, store=ds)
        print("Resource: {}".format(resource))

    def test_create_style(self):
        ws = self.workspace
        sld_file_path = os.path.join(BASE_PATH, "data/c.sld")
        with open(sld_file_path) as f:
            style_name = os.path.basename(sld_file_path).replace('.sld', '')
            style_format = 'sld10'
            self.catalog.create_style(name=style_name,
                                      data=f.read(),
                                      overwrite=True,
                                      workspace=ws,
                                      style_format=style_format)

            style = self.catalog.get_style(style_name, workspace=ws)

            self.assertIsNotNone(style)
            self.assertEqual(style.name, style_name)
            self.assertEqual(style.style_format, style_format)

