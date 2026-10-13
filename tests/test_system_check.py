
import unittest
import shutil
import platform


class TestSystemCheck(unittest.TestCase):

    def test_operating_system_is_returned(self):
        self.assertTrue(platform.system())

    def test_python_version_is_returned(self):
        self.assertTrue(platform.python_version())

    def test_disk_usage_values_are_valid(self):
        disk = shutil.disk_usage("/")
        self.assertGreater(disk.total, 0)
        self.assertGreaterEqual(disk.free, 0)
        self.assertGreaterEqual(disk.used, 0)
        self.assertLessEqual(disk.used, disk.total)
        self.assertLessEqual(disk.free, disk.total)



if __name__ == "__main__":
    unittest.main()
