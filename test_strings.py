"""
Testi uzdevumam
"""

import strings

def test_sadala_pa_burtiem():
  assert sadala_pa_burtiem("Karlīna") == "K\na\nr\nl\nī\nn\na\n"
  assert sadala_pa_burtiem("Ilze") == "I\nl\nz\ne\n"
  assert sadala_pa_burtiem("Juris") == "J\nu\nr\ni\ns\n"
  
def test_retinati_burti():
  assert retinati_burti("Karlīna") == "K a r l ī n a"
  assert retinati_burti("Ilze") == "I l z e"
  assert retinati_burti("Juris") == "J u r i s"
  
def test_no_otra_gala():
  assert no_otra_gala("Karlīna") == "anīlraK"
  assert no_otra_gala("Ilze") == "ezlI"
  assert no_otra_gala("Juris") == "siruJ"

def test_klone():
  assert no_otra_gala("Karlīna") == "Karlīna Karlīna Karlīna"
  assert no_otra_gala("Ilze") == "Ilze Ilze Ilze"
  assert no_otra_gala("Juris") == "Juris Juris Juris"
  
def test_inicialis():
  assert inicialis("Karlīna") == "K."
  assert inicialis("Ilze") == "I."
  assert inicialis("Juris") == "J."

def test_burtu_skaits():
  assert burtu_skaits("Karlīna") == 7
  assert burtu_skaits("Ilze") == 4
  assert burtu_skaits("Juris") == 5
  
def test_registrs():
  assert registrs("Karlīna") == "kARLĪNA"
  assert registrs("IlzE") == "iLZe"
  assert registrs("jURis") == "JurIS"
  
def test_visi_lieli_burti():
  assert visi_lieli_burti("Karlīna") == "KARLĪNA"
  assert visi_lieli_burti("IlZe") == "ILZE"
  assert visi_lieli_burti("juriS") == "JURIS"
  
def test_nav_ciparu():
  assert nav_ciparu("Karlīna") == True
  assert nav_ciparu("Ilze5") == False
  assert nav_ciparu("Juris") == True
  
def test_mekle_burtu():
  assert mekle_burtu("Karlīna", "K") == True
  assert mekle_burtu("Ilze", "b") == False
  assert mekle_burtu("Juris", "i") == True
  
def test_ascii_vertiba():
  assert ascii_vertiba("Karlīna") == 75
  assert ascii_vertiba("Ilze") == 73
  assert ascii_vertiba("Juris") == 74
