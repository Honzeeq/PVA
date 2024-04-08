import math

firstpoint = []

secondpoint = []

sidelength_input = input("room size: ")

is_on_wall_1 = False
is_on_wall_2 = False

if sidelength_input.isnumeric() == False or int(sidelength_input) == 0:
    print("wrong input")
    exit()
else:
    sidelength = int(sidelength_input)

point_input1 = input("point 1: ")
point_input1 = point_input1.split()

for i in point_input1:
    if (i.isnumeric() == False) or (0 < int(i) < 20) or (sidelength - 20 < int(i) > sidelength):
        print("wrong input")
        exit()
    if int(i) == 0 or int(i) == sidelength:
        is_on_wall_1 = True
    if len(point_input1) != 3:
        print("wrong input")
        exit()
if is_on_wall_1 == False:
    print("wrong input")
    exit()
firstpoint = [int(i) for i in point_input1]  

point_input2 = input("point 2: ")
point_input2 = point_input2.split()
for i in point_input2:
    if (i.isnumeric() == False) or (0 < int(i) < 20) or (sidelength - 20 < int(i) > sidelength):
        print("wrong input")
        exit()
    if int(i) == 0 or int(i) == sidelength:
        is_on_wall_2 = True
    if len(point_input2) != 3:
        print("wrong input")
        exit()
if is_on_wall_2 == False:
    print("wrong input")
    exit()
secondpoint = [int(i) for i in point_input2]

def oppositesidecheck(firstpoint, secondpoint, sidelength):
    return (
        (firstpoint[0] == 0 and secondpoint[0] == sidelength) or
        (secondpoint[0] == 0 and firstpoint[0] == sidelength) or
        (firstpoint[1] == 0 and secondpoint[1] == sidelength) or
        (secondpoint[1] == 0 and firstpoint[1] == sidelength) or
        (firstpoint[2] == 0 and secondpoint[2] == sidelength) or
        (secondpoint[2] == 0 and firstpoint[2] == sidelength)
    )

def edge_distances (p, side):
    distances = [p[0], p[1], side - p[0], side - p[1]]
    return distances

def pipecalculation (p1, p2, side):
    if oppositesidecheck(firstpoint, secondpoint, sidelength):
        p1 = [i for i in p1 if (i != 0 and i != side)]
        p2 = [i for i in p2 if (i != 0 and i != side)]
        distances1 = edge_distances(p1, side)
        distances2 = edge_distances(p2, side)
        distances = []
        for i in range(4):
            longer_pendant = distances1[i] + distances2[i] + side
            if i%2 == 0:
                shorter_pendant = abs(p1[1] - p2[1])
            else:
                shorter_pendant = abs(p1[0] - p2[0])
            distances.append(longer_pendant + shorter_pendant)
        distance = min(distances)
    else:
        distance = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
    return distance

def hosecalculation (p1, p2, side):
    if oppositesidecheck(firstpoint, secondpoint, sidelength):
        p1 = [i for i in p1 if (i != 0 and i != side)]
        p2 = [i for i in p2 if (i != 0 and i != side)]
        distances1 = edge_distances(p1, side)
        distances2 = edge_distances(p2, side)
        distances = []
        for i in range(4):
            longer_pendant = distances1[i] + distances2[i] + side
            if i%2 == 0:
                shorter_pendant = abs(p1[1] - p2[1])
            else:
                shorter_pendant = abs(p1[0] - p2[0])
            distances.append(math.sqrt(longer_pendant**2 + shorter_pendant**2))
        distance = min(distances)
    else:
        for i in range(3):
            if p1[i] == 0 or p1[i] == side:
                axis1 = i
            if p2[i] == 0 or p2[i] == side:
                axis2 = i     
        other_axis = [i for i in range(3) if i != axis1 and i != axis2][0]   
        distance = math.sqrt((abs(p1[axis1] - p2[axis1]) + abs(p1[axis2] - p2[axis2]))**2 + abs(p1[other_axis] - p2[other_axis])**2)
    return distance

print(f"Delka trubek: {pipecalculation(firstpoint, secondpoint, sidelength)}")
print(f"Delka hadice: {hosecalculation(firstpoint, secondpoint, sidelength)}")