import unittest
import program


class TestProgram(unittest.Testcase):
    def test_sorting(self):
        self.assertEqual(program.sorting())

if __name__ == '__main__':
    unittest.main()
        