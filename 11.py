kek = """
8577245547
1654333653
5365633785
1333243226
4272385165
5688328432
3175634254
6775142227
6152721415
2678227325
"""


size = len(kek.split("\n")[3])

kek = kek.replace("\n","")
kek = [int(k) for k in kek]

flashes = 0

class octopus:
    def __init__(self, energy):
        self.energy = energy
        self.can_flash = True
        self.nbrs = []

    def step(self):
        global flashes

        if self.can_flash:
            self.energy += 1

        if self.can_flash and self.energy > 9:
            self.can_flash = False
            flashes += 1

            for n in self.nbrs:
                n.step()

    def __repr__(self):
        global kek
        return str((self.energy))

def prnt():
    for i in range(0, len(kek)):
        if i % size == 0:
            print("")
        print(kek[i], end="")
    print("")


for k in kek:
    kek[kek.index(k)] = octopus(int(k))

for k in kek:
    i = kek.index(k)
    for a in (i-size-1, i-size, i-size+1, i-1, i+1, i+size-1, i+size, i+size+1):
        try:
            if a >= 0 and a < 100:
                k.nbrs.append(kek[a])
        except:
            pass


    if i % 10 == 0:
        for ss in (i-size-1, i-1, i+size-1):
            try:
                k.nbrs.remove(kek[ss])
            except:
                pass
                
    if i % 10 == 9:
        for ss in (i-size+1, i+1, i+size+1):
            try:
                k.nbrs.remove(kek[ss])
            except:
                pass


#for p in range(0,100):
for p in range(1,10**10):
    flashed = 0

    for k in kek:
        k.step()


    for k in kek:
        if not k.can_flash:
            flashed += 1
            k.energy = 0
            k.can_flash = True
    print(p)
    if flashed == 100:
        print(p)
        quit()

print("")
print("")
print("")
print(flashes)
