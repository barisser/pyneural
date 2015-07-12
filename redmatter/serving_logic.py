import data

def data_is_present(datahash):
    a = datahash in data.data_hashes
    return a

def handle_redmatter_request(data):
    k = data.keys()
    response = {}
    if 'filehash' in k: #this is a data request
        response = handle_data_request(data)
    elif 'neighborhash' in k:
        response = handle_neighbor_request(data)
    return response

def handle_data_request(request):
    datahash = request['filehash']
    if data_is_present(datahash):
        response['data'] = data.open_file_contents(datahash)
        #response['neighbor'] =
        #response['state'] =
        #response['nexthash'] =
    else:
        response['neighbor'] = -1
        #response['state'] =



def handle_neighbor_request(data):
    k=0

def find_nearest_neighbor_for_filehash(filehash, myhash):
    myn = util.hash_to_int(myhash)
