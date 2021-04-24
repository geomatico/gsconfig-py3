# coding: utf-8

import os

from test.test_catalog import TestCatalogBase, BASE_PATH, DOCKER, DOCKER_MOUNT_FOLDER


class TestCatalogCoverage(TestCatalogBase):

    def test_harvest_externalgranule(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)

        tif_path = os.path.join(BASE_PATH, "data/mosaic/cea_bis_20150101.tif")
        if DOCKER:
            tif_path = os.path.join(DOCKER_MOUNT_FOLDER, "data/mosaic/cea_bis_20150101.tif")
        self.catalog.harvest_externalgranule(
            "file://{}".format(tif_path),
            ds,
        )
        self.catalog.save(ds)

    def test_harvest_uploadgranule(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        tif_path = os.path.join(BASE_PATH, "data/mosaic/cea_bis.zip")
        self.catalog.harvest_uploadgranule(
            "{}".format(tif_path),
            ds,
        )
        self.catalog.save(ds)

    def test_mosaic_coverages(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        mc =self.catalog.mosaic_coverages(ds)

    def test_mosaic_coverage_schema(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        mcs = self.catalog.mosaic_coverage_schema(
            "gsconfig_test_create_imagemosaic",
            ds
        )

    def test_mosaic_granules(self):
        ws = self.workspace
        self.catalog.create_imagemosaic(
            "gsconfig_test_create_imagemosaic",
            os.path.join(BASE_PATH, "data/mosaic/cea.zip"),
            workspace=ws,
        )
        ds = self.catalog.get_store("gsconfig_test_create_imagemosaic",
                                    workspace=ws)
        mg = self.catalog.mosaic_granules(
            "gsconfig_test_create_imagemosaic",
            ds
        )
