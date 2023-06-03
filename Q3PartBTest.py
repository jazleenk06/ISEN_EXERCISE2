import unittest
from Q3PartB import reactor_core_warning

class ReactorCoreWarningTestCase(unittest.TestCase):
    def test_below_300_degrees(self):
        self.assertEqual(reactor_core_warning(299), "Danger! Core temp too low")

    def test_at_300_degrees(self):
        self.assertEqual(reactor_core_warning(300), "Warning! Core temp low. Decreased efficiency.")

    def test_just_below_650_degrees(self):
        self.assertEqual(reactor_core_warning(649), "Warning! Core temp low. Decreased efficiency.")

    def test_at_650_degrees(self):
        self.assertEqual(reactor_core_warning(650), "Reactor core operating at standard temperatures")

    def test_just_below_800_degrees(self):
        self.assertEqual(reactor_core_warning(799), "Reactor core operating at standard temperatures")

    def test_at_800_degrees(self):
        self.assertEqual(reactor_core_warning(800), "Reactor core operating at increased temperatures")

    def test_just_below_950_degrees(self):
        self.assertEqual(reactor_core_warning(949), "Reactor core operating at increased temperatures")

    def test_at_950_degrees(self):
        self.assertEqual(reactor_core_warning(950), "Warning! Core temp High. Deploy control rods.")

    def test_just_below_1100_degrees(self):
        self.assertEqual(reactor_core_warning(1099), "Warning! Core temp High. Deploy control rods.")

    def test_at_1100_degrees(self):
        self.assertEqual(reactor_core_warning(1100), "Danger! Core temp too high")

    def test_above_1100_degrees(self):
        self.assertEqual(reactor_core_warning(1200), "Danger! Core temp too high")

if __name__ == '__main__':
    unittest.main()

