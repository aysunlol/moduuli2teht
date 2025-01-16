import math

sade_str = input("anna ympyrän säde")
sade = float (sade_str)
ala = math.pi * math.pow(sade,2)
print(f"Ympyrän säde on {sade}")
print(f"Ympyrän pinta-ala on {ala:.3f}")
