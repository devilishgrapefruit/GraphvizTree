import unittest

from tree import get_graph

class Test(unittest.TestCase):
    def testCorrectPath(self):
        self.assertEqual(get_graph('D:\\test'), 1)
    def testPathWithWhitespace(self):
        self.assertEqual(get_graph('D:  \\ test'), 1)
    def testPathToFileFromDirectory(self):
        self.assertEqual(get_graph('D:\\Dir_a\\a.txt'), 1)
    def testPathToFileFromDisk(self):
        self.assertEqual(get_graph('D:\\a.txt'), 1)
    def testForErrorPath(self):
        self.assertEqual(get_graph('bddjrrv'), -1)
    def testForPathWithErrorSplit(self):
        self.assertEqual(get_graph('C:\test'), -1)

if __name__ == '__test_tree__':
    unittest.main()

