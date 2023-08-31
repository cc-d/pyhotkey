import json
import os
import unittest
import sys

from utils import read_combos, write_combos

class TestUtils(unittest.TestCase):

    def setUp(self):
        # Create a test file with mock data in the /tmp directory
        self.test_path = '/tmp/test_combos.json'
        self.test_data = {'CTRL+ALT+T': 'Test Text'}
        with open(self.test_path, 'w') as f:
            json.dump(self.test_data, f, indent=4)

    def tearDown(self):
        # Remove the test file
        if os.path.exists(self.test_path):
            os.remove(self.test_path)

    def test_load_combos(self):
        """Test if load_combos correctly loads data."""
        loaded_data = read_combos(file_path=self.test_path)
        self.assertEqual(loaded_data, self.test_data)

    def test_write_combos(self):
        """Test if write_combos correctly writes data."""
        new_data = {'CTRL+ALT+U': 'Updated Test'}
        write_combos(new_data, file_path=self.test_path)

        # Read the file to see if it was correctly written
        with open(self.test_path, 'r') as f:
            updated_data = json.load(f)

        self.assertEqual(updated_data, new_data)



if __name__ == '__main__':
    unittest.main()

