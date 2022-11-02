import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_virheellisella_tilavuudella_nollaa_tilavuuden(self):
        varasto = Varasto(-13)
        self.assertAlmostEqual(varasto.tilavuus, 0.0)

    def test_konstruktori_virheellisella_saldolla_nollaa_saldon(self):
        varasto = Varasto(10, -18)
        self.assertAlmostEqual(varasto.saldo, 0.0)


    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_negatiivinen_lisays_ei_vahenna_maaraa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.lisaa_varastoon(-8)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_liiallinen_lisaaminen_ei_ylita_varaston_kokoa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(str(self.varasto), "saldo = 10, vielä tilaa 0")

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_ottaminen_ei_vaikuta(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-3)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ota_liikaa_palauttaa_koko_varaston(self):
        self.varasto.lisaa_varastoon(10)

        self.assertAlmostEqual(self.varasto.ota_varastosta(13), 10)

    def test_oikea_merkkijonoesitys(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(str(self.varasto), "saldo = 8, vielä tilaa 2")