with open("day6/data.txt", "r") as f:
    data = f.read()
    pos = data.replace("\n", "").find("^")
    map_area = data.split("\n")

# define some helper functions
turn = lambda d: (-d[1], d[0])  # takes the direction tuple and make it turn right
tile_at = lambda p: map_area[p[1]][
    p[0]
]  # gets the map tile at a specific position tuple


def set_tile(p, v):
    return (
        map_area[: p[1]]
        + [(map_area[p[1]][: p[0]] + v + map_area[p[1]][p[0] + 1 :])]
        + map_area[p[1] + 1 :]
    )


add = lambda t1, t2: tuple(
    x + y for x, y in zip(t1, t2)
)  # adds two tuples using vector addition rules

# get some info about the game map
width = len(map_area[0])
height = len(map_area)
pos = (pos % width, pos // width)
dir = (0, -1)  # init the direction as upwards


# take one single step
def take_step():
    global pos, dir, width, height, map_area
    new_pos = add(pos, dir)
    map_area = set_tile(pos, "X")
    if min(new_pos) < 0 or new_pos[0] >= width or new_pos[1] >= height:
        return False  # exit if the guard has hit the edge of the map

    if tile_at(new_pos) == "#":
        dir = turn(dir)
        return True
    else:
        pos = add(pos, dir)
        return True



while take_step(): pass

print("".join(map_area).count("X"))
