"""
Testi uzdevumam
"""

import strings

def test_sadala_pa_burtiem():
  assert strings.sadala_pa_burtiem("Karlīna") == "K\na\nr\nl\nī\nn\na\n"
  assert strings.sadala_pa_burtiem("Ilze") == "I\nl\nz\ne\n"
  assert strings.sadala_pa_burtiem("Juris") == "J\nu\nr\ni\ns\n"
  
def test_retinati_burti():
  assert strings.retinati_burti("Karlīna") == "K a r l ī n a"
  assert strings.retinati_burti("Ilze") == "I l z e"
  assert strings.retinati_burti("Juris") == "J u r i s"
  
def test_no_otra_gala():
  assert strings.no_otra_gala("Karlīna") == "anīlraK"
  assert strings.no_otra_gala("Ilze") == "ezlI"
  assert strings.no_otra_gala("Juris") == "siruJ"

def test_klone():
  assert strings.klone("Karlīna") == "Karlīna Karlīna Karlīna"
  assert strings.klone("Ilze") == "Ilze Ilze Ilze"
  assert strings.klone("Juris") == "Juris Juris Juris"
  
def test_inicialis():
  assert strings.inicialis("Karlīna") == "K."
  assert strings.inicialis("Ilze") == "I."
  assert strings.inicialis("Juris") == "J."

def test_burtu_skaits():
  assert strings.burtu_skaits("Karlīna") == 7
  assert strings.burtu_skaits("Ilze") == 4
  assert strings.burtu_skaits("Juris") == 5
  
def test_registrs():
  assert strings.registrs("Karlīna") == "kARLĪNA"
  assert strings.registrs("IlzE") == "iLZe"
  assert strings.registrs("jURis") == "JurIS"
  
def test_visi_lieli_burti():
  assert strings.visi_lieli_burti("Karlīna") == "KARLĪNA"
  assert strings.visi_lieli_burti("IlZe") == "ILZE"
  assert strings.visi_lieli_burti("juriS") == "JURIS"
  
def test_nav_ciparu():
  assert strings.nav_ciparu("Karlīna") == True
  assert strings.nav_ciparu("Ilze5") == False
  assert strings.nav_ciparu("Juris") == True
  
def test_mekle_burtu():
  assert strings.mekle_burtu("Karlīna", "K") == True
  assert strings.mekle_burtu("Ilze", "b") == False
  assert strings.mekle_burtu("Juris", "i") == True
  
def test_ascii_vertiba():
  assert strings.ascii_vertiba("Karlīna") == 75
  assert strings.ascii_vertiba("Ilze") == 73
  assert strings.ascii_vertiba("Juris") == 74
