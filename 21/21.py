d = 0
rolled = 0
def roll():
    global d
    global rolled

    d += 1
    rolled += 1
    return d

pos = [3, 7]
score = [0, 0]

def turn():
    global pos
    global score

    if score[0] >= 1000 or score[1] >= 1000:
        return False

    a = roll()
    b = roll()
    c = roll()
    add = a+b+c
    pos[0] += add
    pos[0] = pos[0] % 10
    score[0] += pos[0] + 1

    if score[0] >= 1000 or score[1] >= 1000:
        return False

    a = roll()
    b = roll()
    c = roll()
    add = a+b+c
    pos[1] += add
    pos[1] = pos[1] % 10
    score[1] += pos[1] + 1

    return True

while turn():
    pass
print(min(score) * rolled)
