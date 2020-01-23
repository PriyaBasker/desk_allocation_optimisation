import unittest
from src.helper import plots as plot


class TestPlots(unittest.TestCase):
    def test_get_filename(self):
        """if the image and file name created in correct format
        """
        name="test"
        imgname, filename = plot.get_filename(name)
        self.assertTrue("test_plot.png" in imgname)
        self.assertTrue("src/static/images/" in filename)

if __name__ == '__main__':
    unittest.main()