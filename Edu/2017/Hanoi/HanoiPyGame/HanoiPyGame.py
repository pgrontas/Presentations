from helper import init,moveDisk

def towers(nd, source, dest):
    if nd>0:
        temp = 3-source-dest
        towers(nd-1, source, temp)
        moveDisk(source,dest)
        towers(nd-1, temp, dest)

n = 3
init(n)
towers(n,0,2)  