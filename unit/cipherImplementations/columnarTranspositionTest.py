from cipherImplementations.columnarTransposition import ColumnarTransposition
from unit.cipherImplementations.CipherTestBase import CipherTestBase
from util.textUtils import map_text_into_numberspace


class ColumnarTranspositionTest(CipherTestBase):
    cipher = ColumnarTransposition(CipherTestBase.ALPHABET, CipherTestBase.UNKNOWN_SYMBOL, CipherTestBase.UNKNOWN_SYMBOL_NUMBER)
    plaintext = b'filled block'
    key = [3, 1, 2]
    ciphertext = b'ielkldoxflbc'
    decrypted_plaintext = b'filledblockx'

    def test1generate_random_key_allowed_length(self):
        length = 5
        key = self.cipher.generate_random_key(length)
        self.assertEqual(len(key), length)
        alph = list(range(length))
        for c in key:
            self.assertTrue(c in alph)
            alph.remove(c)
        self.assertEqual(alph, [])

        length = 19
        key = self.cipher.generate_random_key(length)
        self.assertEqual(len(key), length)
        alph = list(range(length))
        for c in key:
            self.assertTrue(c in alph)
            alph.remove(c)
        self.assertEqual(alph, [])

        length = 150
        key = self.cipher.generate_random_key(length)
        self.assertEqual(len(key), length)
        alph = list(range(length))
        for c in key:
            self.assertTrue(c in alph)
            alph.remove(c)
        self.assertEqual(alph, [])

    def test2generate_random_key_wrong_length_parameter(self):
        self.run_test2generate_random_key_wrong_length_parameter()

    def test3filter_keep_unknown_symbols(self):
        self.run_test3filter_keep_unknown_symbols()

    def test4filter_delete_unknown_symbols(self):
        self.assertEqual(self.cipher.filter(self.plaintext, keep_unknown_symbols=False), self.decrypted_plaintext.replace(b'x', b''))

    def test5encrypt(self):
        self.run_test5encrypt()

    def test6decrypt(self):
        self.run_test6decrypt()