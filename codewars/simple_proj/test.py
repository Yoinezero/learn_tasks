import unittest
import main as t


class TestDecrypt(unittest.TestCase):
    def test1_decrypt(self):
        self.assertEqual(t.decrypt("This is a test!", 0), "This is a test!")

    def test2_decrypt(self):
        self.assertEqual(t.decrypt("hsi  etTi sats!", 1), "This is a test!")

    def test3_decrypt(self):
        self.assertEqual(t.decrypt("s eT ashi tist!", 2), "This is a test!")

    def test4_decrypt(self):
        self.assertEqual(t.decrypt(" Tah itse sits!", 3), "This is a test!")

    def test5_decrypt(self):
        self.assertEqual(t.decrypt("This is a test!", 4), "This is a test!")

    def test6_decrypt(self):
        self.assertEqual(t.decrypt("This is a test!", -1), "This is a test!")

    def test7_decrypt(self):
        self.assertEqual(t.decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")


class TestEncrypt(unittest.TestCase):
    def test1_encrypt(self):
        self.assertEqual(t.encrypt("This is a test!", 0), "This is a test!")

    def test2_encrypt(self):
        self.assertEqual(t.encrypt("This is a test!", 1), "hsi  etTi sats!")

    def test3_encrypt(self):
        self.assertEqual(t.encrypt("This is a test!", 2), "s eT ashi tist!")

    def test4_encrypt(self):
        self.assertEqual(t.encrypt("This is a test!", 3), " Tah itse sits!")

    def test5_encrypt(self):
        self.assertEqual(t.encrypt("This is a test!", 4), "This is a test!")

    def test6_encrypt(self):
        self.assertEqual(t.encrypt("This is a test!", -1), "This is a test!")

    def test7_encrypt(self):
        self.assertEqual(t.encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")


if __name__ == '__main__':
    unittest.main()
