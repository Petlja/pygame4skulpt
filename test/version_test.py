import pygame as pg
import unittest


class TestingPygameVersion(unittest.TestCase):
    def test_ver(self):
        self.assertIsInstance(pg.version.ver, str)

    def test_vernum(self):
        self.assertIsInstance(pg.version.vernum, tuple)
        self.assertEqual(len(pg.version.vernum), 3)
        for i in range(3):
            self.assertIsInstance(pg.version.vernum[i], int)

    def test_rev(self):
        self.assertEqual(pg.version.rev, "")


if __name__ == '__main__':
    pg.init()
    unittest.main()
    pg.quit()
