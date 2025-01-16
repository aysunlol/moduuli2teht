import math

pintaala_str = input ("Mika on suorakulmion kanta?")
pintaala_str = input ("Mikä on suorakulmion korkeus?")
kanta = float(input("kanta"))
korkeus = float(input("korkeus"))
piiri = float(input("piiri"))
pintaala = float(input("pintaala"))
piiri = 2 * kanta + 2 * korkeus
pintaala = kanta * korkeus
print(f"Suorakulmion piiri on {piiri=}")
print(f"Suorakulmion pinta-ala on {pintaala}")