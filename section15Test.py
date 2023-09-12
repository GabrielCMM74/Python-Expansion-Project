import unittest
import section15


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = section15.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'sdfsdf'
        result = section15.do_stuff(test_param)
        self.assertTrue(isinstance(result, ValueError))

    def test_do_stuff3(self):
        test_param = None
        result = section15.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = section15.do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


if __name__ == '__main__':
    unittest.main()
