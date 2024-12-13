# I messed this up and cant work out what i was trying to do and will maybe fix at some point lol

with open("day6/test_data.txt", "r") as f:
    data = f.read()
    pos = data.replace("\n", "").find("^")
    map_area = data.split("\n")

# define some helper functions


add = lambda t1, t2: tuple(
    x + y for x, y in zip(t1, t2)
)  # adds two tuples using vector addition rules

# get some info about the game map
width = len(map_area[0])
height = len(map_area)
pos = (pos % width, pos // width)
dir = (0, -1)  # init the direction as upwards


# take one single step
def take_step(map_area, pos, dir, visited):
    global width, height

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

    new_pos = add(pos, dir)
    map_area = set_tile(pos, "X")
    if min(new_pos) < 0 or new_pos[0] >= width or new_pos[1] >= height:
        return (False, False)  # exit if the guard has hit the edge of the map
    if (new_pos, dir) in visited:
        return (False, True)

    visited.append((new_pos, dir))

    if tile_at(new_pos) == "#":
        dir = turn(dir)
        return (True, False)
    else:
        pos = add(pos, dir)
        return (True, False)


def test(map_state, test_pos):
    global pos, dir
    pos1 = pos
    dir1 = dir
    visited = []
    test_map = map_state.copy()
    test_map = (
        test_map[: test_pos[1]]
        + [
            (
                test_map[test_pos[1]][: test_pos[0]]
                + "#"
                + test_map[test_pos[1]][test_pos[0] + 1 :]
            )
        ]
        + test_map[test_pos[1] + 1 :]
    )
    while (res := take_step(test_map, pos1, dir1, visited))[0]:
        pass
    return res[1]


print(test(map_area, (0, 0)))
