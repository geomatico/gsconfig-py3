# coding: utf-8

import os
from test.test_catalog import TestCatalogBase, DB_PARAMS, BASE_PATH, DOCKER_MOUNT_FOLDER, DOCKER


class TestCatalogDatastore(TestCatalogBase):

    def test_create_datastore(self):
        ws = self.workspace
        ds = self.catalog.create_datastore(
            "gsconfig_test_datastore",
            workspace=ws
        )
        self.catalog.save(ds)
        l_ds = self.catalog.get_store(
            "gsconfig_test_datastore",
            workspace=ws
        )
        self.assertIsNotNone(l_ds)
        self.assertEqual(l_ds.name, "gsconfig_test_datastore")
        self.assertEqual(l_ds.workspace, ws)

    def test_create_coveragestore2(self):
        ws = self.workspace
        ds = self.catalog.create_coveragestore2(
            "gsconfig_test_coveragestore2",
            workspace=ws
        )
        self.catalog.save(ds)
        l_ds = self.catalog.get_store(
            "gsconfig_test_coveragestore2",
            workspace=ws
        )
        self.assertIsNotNone(l_ds)
        self.assertEqual(l_ds.name, "gsconfig_test_coveragestore2")
        self.assertEqual(l_ds.workspace, ws)

    def test_create_wmsstore(self):
        ws = self.workspace
        ds = self.catalog.create_wmsstore(
            "gsconfig_test_wmsstore",
            workspace=ws
        )
        self.catalog.save(ds)
        l_ds = self.catalog.get_store(
            "gsconfig_test_wmsstore",
            workspace=ws
        )
        self.assertIsNotNone(l_ds)
        self.assertEqual(l_ds.name, "gsconfig_test_wmsstore")
        self.assertEqual(l_ds.workspace, ws)

    def test_import_data_to_created_datastore(self):
        ws = self.workspace
        ds = self.catalog.create_datastore("gsconfig_import_test",
                                           workspace=ws)
        ds.connection_parameters.update(**DB_PARAMS)
        self.catalog.save(ds)
        ds = self.catalog.get_store("gsconfig_import_test", workspace=ws)
        self.catalog.add_data_to_store(ds, "import", {
            'shp': os.path.join(BASE_PATH, 'data/states.shp'),
            'shx': os.path.join(BASE_PATH, 'data/states.shx'),
            'dbf': os.path.join(BASE_PATH, 'data/states.dbf'),
            'prj': os.path.join(BASE_PATH, 'data/states.prj'),
        })

    def test_create_featurestore(self):
        ws = self.workspace
        self.catalog.create_featurestore(
            "gsconfig_test_create_featurestore",
            {
                'shp': os.path.join(BASE_PATH, 'data/states.shp'),
                'shx': os.path.join(BASE_PATH, 'data/states.shx'),
                'dbf': os.path.join(BASE_PATH, 'data/states.dbf'),
                'prj': os.path.join(BASE_PATH, 'data/states.prj'),
            },
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_featurestore",
                                    workspace=ws)

    def test_create_imagemosaic(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)

    def test_create_coveragestore(self):
        ws = self.workspace
        self.catalog.create_coveragestore(
            "gsconfig_test_create_coveragestore",
            {
                'tiff': os.path.join(BASE_PATH, 'data/Pk50095.tif'),
                'tfw':  os.path.join(BASE_PATH, 'data/Pk50095.tfw'),
                'prj':  os.path.join(BASE_PATH, 'data/Pk50095.prj'),
            },
            workspace=ws,
        )

    def test_create_coveragestore_external_geotiff(self):
        ws = self.workspace
        tif_path = os.path.join(BASE_PATH, "data/Pk50095.tif")
        if DOCKER:
            tif_path = os.path.join(DOCKER_MOUNT_FOLDER, "data/Pk50095.tif")
        self.catalog.create_coveragestore_external_geotiff(
            "gsconfig_test_create_coveragestore_ext_geotiff",
            "file:{}".format(tif_path),
            workspace=ws
        )
