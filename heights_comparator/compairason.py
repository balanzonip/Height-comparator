import csv
import matplotlib.pyplot as plt

file1 = "other_heights.csv"
file2 = "your_height.csv"

YH = []
S = []
MH = []
Y =[]


with open(file1, newline="",encoding="utf-8") as file:
    nw = csv.DictReader(file)
    for riga in nw:
        S.append(riga["stuff_to_compare"])
        MH.append(float(riga["meters"]))

with open(file2, newline="",encoding="utf-8") as file:
    nw2 = csv.DictReader(file)
    for riga in nw2:
        YH.append(float(riga["your_height"]))
        Y.append(riga["you"])

if not YH:
    raise ValueError("file doesnt contain your height")

asse_y = YH + MH 
asse_x = Y + S
plt.figure (figsize=(9, 4))
plt.plot(asse_x,asse_y, marker="o")
plt.title("Let's see how tall you are")
plt.xlabel("Things")
plt.ylabel("Meters")
plt.legend()
plt.tight_layout()
plt.show()
