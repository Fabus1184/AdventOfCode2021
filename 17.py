pos = ()
vel = ()
trail = []
target_range = ()

def step():
    global pos
    global vel

    trail.append(pos)

    pos = (pos[0]+vel[0], pos[1]+vel[1])

    if vel[0] > 0:
        vel = (vel[0]-1, vel[1])
    if vel[0] < 0:
        vel = (vel[0]+1, vel[1])

    vel = (vel[0], vel[1]-1)

def draw():
    (minx, maxx) = (min(pos[0], vel[0], min([k[0] for k in target]), min([k[0] for k in trail])), max(pos[0], vel[0], max([k[0] for k in target]), max([k[0] for k in trail])))
    (miny, maxy) = (min(pos[1], vel[1], min([k[1] for k in target]), min([k[1] for k in trail])), max(pos[1], vel[1], max([k[1] for k in target]), max([k[1] for k in trail])))

    for y in range(maxy, miny-1, -1):
        for x in range(minx, maxx+1):
            if (x,y) in trail:
                print("#", end="")
                continue
            if (x,y) == pos:
                print("A", end="")
                continue
            if (x,y) in target:
                print("T", end="")
                continue
            if (x,y) == (0,0):
                print("S", end="")
                continue
            print(".", end="")
        print("")

pos = (0, 0)

def test():
    global pos
    global vel
    global target_range
    global target
    pos = (0,0)
    vel = (7, 2)
    target_range = ((20,30), (-10, -5))
    target = [(x,y) for x in range(target_range[0][0], target_range[0][1]+1) for y in range(target_range[1][0], target_range[1][1]+1)]

def a1():
    global pos
    global vel
    global target_range
    global target
    global trail
    pos = (0,0)
    vel = (7, 2)
    target_range = ((185,221), (-122,-74))
    target = [(x,y) for x in range(target_range[0][0], target_range[0][1]+1) for y in range(target_range[1][0], target_range[1][1]+1)]
    trail = []

def brute1():
    global vel
    r = (18, 600)
    ss = 1
    works = ()
    highesty = 0
    for (x,y) in [(x,y) for x in range(r[0], r[1], ss) for y in range(r[0], r[1], ss)]:
        a1()
        vel = (x,y)
        print("%s %s" % ((x,y), str(highesty)))
        for _ in range(1000):
            if pos in target:
                if abs(max([k[1] for k in trail])) > highesty:
                    works = pos
                    highesty = abs(max([k[1] for k in trail]))
            else:
                step()
        print(pos)

a1()
vel = (30,10)

for x in range(200):
    if pos[1] == 0:
        print(pos)
    step()

a1()
init = (20, -5)
vel = tuple(init)

for x in range(20):
    print("Point({%s})" % str(pos))
    step()
