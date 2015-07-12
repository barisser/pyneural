import hashlib
import os

file_path = './public'

def get_filenames():
    return os.listdir(file_path)

def data_hashes():
    a = get_filenames()
    b = []
    for x in a:
        r = x.index('.')
        g = x[0:r]
        b.append(g)
    return b

def open_file_contents(datahash):
    r = datahash + ".txt"
    a = open(r)
    b = a.read()
    return str(b)

def try_generate_identity():
    if 'identity.txt' in get_filenames():
        k=-1
    else:
        #generate new identity()
        generate_identity()

def random_identity():
    return hashlib.sha256(str(os.urandom(50))).hexdigest()

def generate_identity():
    filename = file_path + '/identity.txt'
    file=open(filename, 'w')
    identity = random_identity()
    file.write(identity)
    file.close()

def fetch_identity():
    filename = file_path + '/identity.txt'
    file=open(filename)
    a = file.readline()
    file.close()
    return a
