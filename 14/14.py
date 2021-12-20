import itertools
soos = "SHHBNFBCKNHCNOSHHVFF"
kek = """
CK -> N
VP -> B
CF -> S
FO -> V
VC -> S
BV -> V
NP -> P
SN -> C
KN -> V
NF -> P
SB -> C
PC -> B
OB -> V
NS -> O
FH -> S
NK -> S
HO -> V
NV -> O
FV -> O
FB -> S
PS -> S
FN -> K
HS -> O
CB -> K
HV -> P
NH -> C
BO -> B
FF -> N
PO -> F
BB -> N
PN -> C
BP -> C
HN -> K
CO -> P
BF -> H
BC -> S
CV -> B
VV -> F
FS -> B
BN -> P
VK -> S
PV -> V
PP -> B
PH -> N
SS -> O
SK -> S
NC -> P
ON -> F
NB -> N
CC -> N
SF -> H
PF -> H
OV -> O
KH -> C
CP -> V
PK -> O
KC -> K
KK -> C
KF -> B
HP -> C
FK -> H
BH -> K
VN -> H
OO -> S
SC -> K
SP -> B
KO -> V
KV -> F
HK -> N
FP -> N
NN -> B
VS -> O
HC -> K
BK -> N
KS -> K
VB -> O
OH -> F
KB -> F
KP -> H
HB -> N
NO -> N
OF -> O
BS -> H
VO -> H
SH -> O
SV -> K
HF -> C
CS -> F
FC -> N
VH -> H
OP -> K
OK -> H
PB -> K
HH -> S
OC -> V
VF -> B
CH -> K
CN -> C
SO -> P
OS -> O
""".split("\n")
kek.remove("")
kek.remove("")


def a1(steps):
    global soos
    global r
    r = {}
    for k in kek:
        ss = k.split(" -> ")
        r[ss[0]] = str(ss[0][0]) + str(ss[1]) + str(ss[0][1])    
    
    for i in range(0,steps):
        ss = [(r.get(soos[i:i+2])) for i in range(0, len(soos) - 1)]

        for s in range(0, len(ss) - 1):
            ss[s] = ss[s][0:2]

        soos = "".join(ss)
        
    qty = [soos.count(s) for s in soos]
    print(max(qty) - min(qty), end=",\n")

def a2(steps):
    r = {}
    for k in kek:
        ss = k.split(" -> ")
        r[ss[0]] = str(ss[0][0]) + str(ss[1]) + str(ss[0][1])

    count = {}
    [(count.__setitem__("%s%s" % (l[0], l[1]), 0), count.__setitem__("%s%s" % (l[1], l[0]), 0)) for l in list(itertools.combinations([x for x in list(set("".join(r.keys()))) for _ in range(2)], 2))]
    leer = dict(count)

    [count.__setitem__(soos[i:i+2], count[soos[i:i+2]] + 1) for i in range(len(soos) - 1)]

    for i in range(steps):
        out = dict(leer)
        for k in dict(count):
            [out.__setitem__(r.get(k)[z:z+2], out[r.get(k)[z:z+2]] + count[k]) for z in range(2)]
        count = dict(out)

    qty = {}
    [qty.__setitem__(k, 0) if k not in (soos[0], soos[-1]) else qty.__setitem__(k, 1) for k in list(set("".join(leer)))]

    for q in dict(qty):
        for k in count:
            if q in k:
                qty[q] += count[k] * k.count(q)

    print((max([qty[q] for q in qty]) - min([qty[q] for q in qty])) // 2)

a2(40)
