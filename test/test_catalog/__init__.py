# coding: utf-8

import unittest
import os

import psycopg2

from geoserver.catalog import Catalog
from test import settings


DOCKER = True
DOCKER_MOUNT_FOLDER = '/tmp'

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

# Test database parameters
_HOST = "postgis"
_PORT = "5432"
_DB_TYPE = "postgis"
_DATABASE = os.getenv("DATABASE", "gsconfig_test")
_USER = os.getenv("DBUSER", "gsconfig")
_PASSWORD = os.getenv("DBPASS", "gsconfig")

DB_PARAMS = {
    'host': _HOST,
    'port': _PORT,
    'dbtype': _DB_TYPE,
    'database': _DATABASE,
    'user': _USER,
    'passwd': _PASSWORD,
}


class TestCatalogBase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    # @classmethod
    # def tearDownClass(cls):
    #     sql = """SELECT relname FROM pg_class
    #                 WHERE relkind = 'r' AND relname !~ '^(pg_|sql_)'
    #                     AND relname != 'spatial_ref_sys';"""
    #     conn = psycopg2.connect(
    #         database=_DATABASE,
    #         user=_USER,
    #         password=_PASSWORD,
    #         host=_HOST,
    #         port=_PORT
    #     )
    #     cur = conn.cursor()
    #     cur.execute(sql)
    #     tables = [r[0] for r in cur.fetchall()]
    #     if len(tables) == 0:
    #         return
    #     cur.execute("DROP TABLE {};".format(','.join(tables)))
    #     conn.commit()

    def setUp(self):
        self.catalog = Catalog(settings.SERVICE_URL)
        self.workspace = self.catalog.create_workspace("gsconfig_test")

    def tearDown(self):
        self.catalog.delete(self.workspace, recurse=True)
