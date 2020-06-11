from file_class import *
import unittest


class FileTest(unittest.TestCase):
    def setUp(self):
        self.file_1 = FileFunction('players.txt')

    def test_read_file(self):
        self.assertEqual(self.file_1.read_file(), ['Van Dijk', 'Henderson', 'Firmino', 'Salah', 'Mane', 'Wijnaldum', 'Fabinho', 'Trent', 'Robertson', 'Gomez', 'Allison', 'Keita', 'Chamberlain', 'Origi'])

    def test_print_file(self):
        self.assertEqual(self.file_1.print_file(), """Van Dijk
Henderson
Firmino
Salah
Mane
Wijnaldum
Fabinho
Trent
Robertson
Gomez
Allison
Keita
Chamberlain
Origi""")

    def test_add_to_file(self):
        self.file_1.add_to_file('Origi')
        self.assertEqual(self.file_1.read_file(), ['Van Dijk', 'Henderson', 'Firmino', 'Salah', 'Mane', 'Wijnaldum', 'Fabinho', 'Trent', 'Robertson', 'Gomez', 'Allison', 'Keita', 'Chamberlain', 'Origi'])

    def test_check_file(self):
        self.assertEqual(self.file_1.test_file("aplyer.txt"), False)
