import json
from mpi4py import MPI
import os
import requests

def main():
    # Connect mpi
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    # Get file name
    filename = 'twitter-huge.json'
    # Divide the file evenly into SIZE parts, and the size of each RANK to be read is read_part
    read_part = os.stat(filename).st_size//size

    with open(filename) as f:
        while True:
            response = requests.get('http://admin:15011010377@172.26.135.96:5984/_all_dbs')     

            with open('/Users/waji/Desktop/json_try/sprt_data.json') as f:
                data = json.load(f)

            headers = {'Content-type': 'application/json'}

            for item in data:
                response = requests.post('http://admin:15011010377@172.26.135.96:5984/test', headers = headers, json=item)

    return None

# Run the actual program
if __name__ == "__main__":
    #start_time = time.time()
    main()
    #print("Tottal time is : ", str(time.time()-start_time))