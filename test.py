from vigenere import Vigenere
from autokey_vigenere import AutoKeyVigenere
from full_vigenere import Full_Vigenere
from playfair import Playfair
from extended_vigenere import ExtendedVigenere

vigenere1 = Vigenere()

vigenere1.encrypt("thisplaintext","sony")
print(vigenere1.input)
print(vigenere1.key)
vigenere1.encrypt("Adrian lahir tanggal 18 Juli 2000 !@$%^&*()","adrian")
 
vigenere1.decrypt("AGIQA ALDYQ RGAQX OAYJX CQ","adrian")

autokey = AutoKeyVigenere()
autokey.encrypt("thisisplaintext","sony")
autokey.decrypt("LVVQB ZXDIA CEEFG","sony")

full = Full_Vigenere()
full.generate_table()
full.encrypt("thisisplainhellotext","sony")
storedstring = full.output
full.decrypt(storedstring,"sony")

playfair = Playfair()
playfair.encrypt("temuiibunantimalam","jalanganeshasepuluh")
playfair.decrypt("ZBRSFYKUPGLGRKVSNLQV","jalanganeshasepuluh")

extended = ExtendedVigenere()
extended.encrypt("negarapenghasilminyak","kemanusiaanyangadilda")
storedencrypt = extended.output
extended.decrypt(extended.output,"kemanusiaanyangadilda")

# playfair.create_bigram("")


# vigenere1.printTable()