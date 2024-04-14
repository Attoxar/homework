import unittest
from tv_controller_sub_app import TVController


class TestTVController(unittest.TestCase):
    def setUp(self):
        self.channels = ["BBC", "Discovery", "TV1000"]
        self.controller = TVController(self.channels)

    def test_first_channel(self):
        self.assertEqual(self.controller.first_channel(), "BBC")

    def test_last_channel(self):
        self.assertEqual(self.controller.last_channel(), "TV1000")

    def test_turn_channel(self):
        self.assertEqual(self.controller.turn_channel(1), "BBC")
        self.assertEqual(self.controller.turn_channel(4), "BBC")
        self.assertEqual(self.controller.turn_channel(2), "Discovery")

    def test_next_channel(self):
        self.assertEqual(self.controller.next_channel(), "Discovery")

    def test_previous_channel(self):
        self.controller.turn_channel(3)
        self.assertEqual(self.controller.previous_channel(), "Discovery")

    def test_current_channel(self):
        self.assertEqual(self.controller.current_channel(), "BBC")

    def test_is_exist(self):
        self.assertEqual(self.controller.is_exist("BBC"), "Yes")
        self.assertEqual(self.controller.is_exist(4), "No")


if __name__ == '__main__':
    unittest.main()
