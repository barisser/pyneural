import data

class Neighbor:
    def __init__(self, ip, hash):
        self.ip = ip
        self.hash = hash

def load_neighbors():
    filename = data.file_path + '/neighbors.txt'
    file = open(filename)
    r = file.read()
    r = r.split('\n')
    a = []
    for x in r:
        if len(x) > 0:
            a.append(x)
    return a

def return_neighbor_objects():
    n = load_neighbors()
    a = []
    for x in n:
        c = x.split(' ')
        ip = c[0]
        hash = c[1]
        b = Neighbor(ip, hash)
        a.append(b)
    return a
