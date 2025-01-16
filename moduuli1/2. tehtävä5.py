
leiviskat = input("leiviskat:")
leiviskat = float (leiviskat)
naulat = float(input("Naulat:"))
luodit = float(input("luodit:"))

LUODIT_GR = 13.3
NAULAR_GR = 32 * LUODIT_GR
LEIVISKAT_GR = 20 * NAULAR_GR

massa_gr = LEIVISKAT_GR * leiviskat + NAULAR_GR * naulat + LUODIT_GR * luodit


kilogrammat = int(massa_gr / 1000)
grammat = int(massa_gr % 1000)

print(f"Massa nykytoiminnossa on {kilogrammat} kg ja {grammat:6.2f} g")
