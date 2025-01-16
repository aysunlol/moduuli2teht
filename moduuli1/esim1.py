nimi = ("Matti")
print("Moi + nimi + ",Mitä kuuluu"")
print(f"Moi "{nimi}, kuinkas nyt menee")

# käyttäjän syötteen lukeminen
# huom: input lukee kaikki syötteet
# aina merkkijonoina
lukuA_str = input("Anna kokonaisluku:)"
# muunnetaan merkkijono kokonaisluvuksi
LukuA = int(lukuA_str)
# luen luvun suoraan lukuna
# huom +input
lukuB = input("Anna toinen luku: ")
summa = lukuA + lukuB
print(f"Lukujesi summa = {summa}"
      f")
