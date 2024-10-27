# test_main.py
import unittest
from mylib.lib import hash_sha256, hash_md5


class TestHashFunctions(unittest.TestCase):
    def test_sha256(self):
        """Test SHA-256 hashing with known input."""
        data = "test"
        expected = "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
        self.assertEqual(hash_sha256(data), expected)

    def test_md5(self):
        """Test MD5 hashing with known input."""
        data = "test"
        expected = "098f6bcd4621d373cade4e832627b4f6"
        self.assertEqual(hash_md5(data), expected)


if __name__ == "__main__":
    unittest.main()
