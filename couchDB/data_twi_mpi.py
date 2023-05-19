from mpi4py import MPI
import ijson
import requests
import couchdb

ip = '172.26.135.96'

def check_create_db():
    couch = couchdb.Server(f'http://admin:15011010377@{ip}:5984/')
    
    if 'twi_dbs' in couch:
        del couch['twi_dbs']
    
    couch.create('twi_dbs')

def master_tweet_processor(comm,twi_file_name): 

    size = comm.Get_size()
    with open(twi_file_name) as f:
        objects = ijson.items(f, 'item')
        block_data = []
        while True:
            try:
                data = objects.__next__()
                block_data.append(data)
            except StopIteration as e:
                break
    print(len(block_data))

    split_data = []
    for i in range(0, size):
        if i == size-1:
            block_size = len(block_data) // size + len(block_data) % size
        else:
            block_size = len(block_data) // size
        start = i * (len(block_data) // size)
        end = start + block_size
        split_data.append(block_data[start:end])
    local_data = comm.scatter(split_data, root = 0)

    response = requests.get(f'http://admin:15011010377@{ip}:5984/_all_dbs')
    headers = {'Content-type': 'application/json'}

    for item in local_data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/twi_dbs', headers = headers, json=item)


def slave_tweet_processor(comm):
    receive_data = comm.scatter(None, root = 0)

    response = requests.get(f'http://admin:15011010377@{ip}:5984/_all_dbs')

    headers = {'Content-type': 'application/json'}

    for item in receive_data:
        response = requests.post(f'http://admin:15011010377@{ip}:5984/twi_dbs', headers = headers, json=item)

    return None


def main():
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    if rank == 0 :
        check_create_db()

    # Get file name
    twi_file_name = "sport_data.json"

    if rank == 0 :
        # We are master
        master_tweet_processor(comm, twi_file_name)
    else:
        # We are slave
        slave_tweet_processor(comm)

# Run the actual program
if __name__ == "__main__":
    main()