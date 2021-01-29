from vigenere import Vigenere

vigenere1 = Vigenere()

vigenere1.encrypt("thisplaintext","sony")
vigenere1.encrypt("Adrian lahir tanggal 18 Juli 2000 !@$%^&*()","adrian")

vigenere1.decrypt("AGIQA ALDYQ RGAQX OAYJX CQ","adrian")

# vigenere1.printTable()