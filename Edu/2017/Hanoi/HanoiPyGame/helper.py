game = [[],[],[]]
move = 0
stepbystep=True 

def init(n):
    global move
    move=0
    for i in range(n,0,-1):
        game[0].append(i)
    print("Initial State:", game)

def towerFromIndex(i):
    if i == 0:
        return "tower A"
    elif i==1:
        return "tower B"
    else:
        return "tower C"

def moveDisk(fromTower,toTower):
    global move
    global stepbystep
    move+=1
    x=game[fromTower].pop()
    game[toTower].append(x)
    print("Move ",move, "Moving disk: ", x, "from ", towerFromIndex(fromTower), "to ", towerFromIndex(toTower))
    print("Tower A:", game[0])
    print("Tower B:", game[1])
    print("Tower C:", game[2])
    if stepbystep:
        input("Press to continue...")
