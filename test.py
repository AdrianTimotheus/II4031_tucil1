from vigenere import Vigenere
from autokey_vigenere import AutoKeyVigenere
from full_vigenere import Full_Vigenere

vigenere1 = Vigenere()

vigenere1.encrypt("thisplaintext","sony")
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


# vigenere1.printTable()