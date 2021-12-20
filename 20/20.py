import copy

l = 0
def test():
    global algorithm
    global image
    global l
    l = 5
    algorithm = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..##
#..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###
.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#.
.#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#.....
.#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#..
...####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.....
..##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#
""".split("\n")
    algorithm.remove("")
    algorithm.remove("")
    algorithm = "".join([k for k in algorithm])

    image = """
#..#.
#....
##..#
..#..
..###
""".split("\n")
    image.remove("")
    image.remove("")
    image = "".join([k for k in image])


def visible(image):
    [print(k) for k in image]
    
def imagify(image):
    global l
    return [image[i*l:(i+1)*l] for i in range(len(image) // l)]

def intify(string):
    if string == ".":
        return "0"
    if string == "#":
        return "1"
    return None

def expand(image):
    image = ["." * len(image[0])] + image
    image = image + ["." * len(image[0])]

    for k in image:
        image[image.index(k)] = "." + k + "."


def enhance(image):
    global l
    expand(image)
    expand(image)
    expand(image)
    expand(image)
    expand(image)
    expand(image)

    new_image = copy.deepcopy(image)
    expand(new_image)
    expand(new_image)
    expand(new_image)
    expand(new_image)
    
    for k in new_image:
        new_image[new_image.index(k)] = "." + k + "."


    for line in range(1, len(image) - 1):
        for col in range(1, len(image[0]) - 1):
            b = ""
            b += intify(image[line-1][col-1])
            b += intify(image[line-1][col])
            b += intify(image[line-1][col+1])
            b += intify(image[line][col-1])
            b += intify(image[line][col])
            b += intify(image[line][col+1])
            b += intify(image[line+1][col-1])
            b += intify(image[line+1][col])
            b += intify(image[line+1][col+1])

            new_image[line] = new_image[line][:col] + algorithm[int(b, 2)] + new_image[line][col+1:]


    return new_image
        
test()
image = imagify(image)

image = enhance(image)
visible(image)
