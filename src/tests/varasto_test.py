"""Varasto-luokan toimintojen yksikkötestit"""
import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """Testaa Varasto-luokan toimintaa"""    
    def setUp(self):
        """Alustaa uuden tyjän varaston jokaista testiä varten"""
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """Testaa, että konstruktori lyo tyhjän varaston"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_nollaa_virheellisen_tilavuuden(self):
        """Testaa virheellisen tilavuuden nollaamisen"""
        varasto = Varasto(0)

        self.assertEqual(varasto.tilavuus, 0)

    def test_konstruktori_nollaa_negatiivisen_alkusaldon(self):
        """Testaa negatiivisen alkusaldon nollaamisen"""
        varasto = Varasto(10, -5)

        self.assertEqual(varasto.saldo, 0)

    def test_konstruktori_tayttaa_varaston_jos_alkusaldo_yli_tilavuuden(self):
        """Testaa, ettei alkusaldo ylitä varaston tilavuutta"""
        varasto = Varasto(10, 15)

        self.assertEqual(varasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """Testaa uuden varaston tilavuuden"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """Testaa varastoon lisäämistä"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """Testaa, että lisääminen vähentää vapaata tilaa"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """Testaa varastosta otetun määrän palauttamista"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """Testaa, että varastosta ottaminen lisää vapaata tilaa"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_lisays_yli_saldon(self):
        """Testaa, ettei varastoon voi lisätä yli tilavuuden"""
        self.varasto.lisaa_varastoon(15)

        self.assertEqual(self.varasto.saldo, 10)

    def test_ottaminen_yli_saldon(self):
        """Testaa, ettei varastosta voi ottaa yli saldon"""
        self.varasto.lisaa_varastoon(5)

        saatu_maara = self.varasto.ota_varastosta(20)

        self.assertEqual(saatu_maara, 5)
        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivisen_maaran_lisaaminen_ei_muuta_saldoa(self):
        """Testaa, ettei negatiivisen määrän lisääminen muuta saldoa"""
        self.varasto.lisaa_varastoon(-5)

        self.assertEqual(self.varasto.saldo, 0)

    def test_negatiivisen_maaran_ottaminen_palauttaa_nollan(self):
        """Testaa, että negatiivisen määrän ottaminen palauttaa nollan"""
        saatu_maara = self.varasto.ota_varastosta(-5)

        self.assertEqual(saatu_maara, 0)
        self.assertEqual(self.varasto.saldo, 0)

    def test_str_palauttaa_oikean_merkkijonon(self):
        """Testaa Varasto-olion merkkijonomuotoa"""
        tulos = str(self.varasto)

        self.assertEqual(tulos, "saldo = 0, vielä tilaa 10")
