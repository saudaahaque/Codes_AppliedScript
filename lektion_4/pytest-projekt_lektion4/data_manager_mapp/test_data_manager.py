
import pytest
from data_manager import frukter, frukt_priser


def test_minsta_värdet():
   first = frukter()[0]
   assert first == "apelsin"


def test_längden_värdet():
   length_of_list = len(frukter())
   assert length_of_list == 5


def test_finns_listan():
   assert "äpple" in frukter()


# dic

def nycklarna_finns():
   rätt_nycklar = {"apelsin", "päron", "vindruvor"}
   assert set(frukt_priser.keys()) == rätt_nycklar


def nycklarna_värde():
   förväntade_värde = {"apelsin": 32, "päron": 31, "vindruvor": 20}
   assert frukt_priser == förväntade_värde


def existans():
   assert "apelsin" in frukt_priser