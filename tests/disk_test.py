## Disk Test

from cgi import test
import unittest
from test import support


class TestDisk(unittest.TestCase):
    #initialize the test disk
    test_Disk = Disk('test_name')
    test_Disk2 = Disk()

    #testing the constructor
        #cases: makes sure that the attributes are correctly stored when the name is explicitly and implicitly stated in the parameter
    def test_constructor(self):
        self.assertEqual(test_Disk.name, 'test_name', 'Failed test_constructor: disk name assigned')
        self.assertEqual(test_Disk2.name, 'Untitled', 'Failed test_constructor: disk name unassigned')
        self.assertEqual(test_Disk.block_size, 1, 'Failed test_constructor: block size')
        self.assertEqual(test_Disk.size, 1000, 'Failed test_constructor: disk size') 

    def test_print(self):
        self.assertEqual(test_Disk.print(), , 'Incorrect map #1')

    def test_delete(self):
        self.assertEqual(test_Disk.delete(), null, 'Failed test_delete: must be null')


if __name__ == "__main__":
    unittest.main()



