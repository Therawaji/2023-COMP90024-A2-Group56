#!/bin/bash

# Run the script to upload twi data to main CouchDB
echo "data_twi_mpi start"
mpiexec -n 2 python3 data_twi_mpi.py
echo "data_twi_mpi finish"

# Run the script to upload external data to main CouchDB
python3 data_push_external.py

# Run the script that does the mapreduce of the data in CouchDB
python3 data_map_reduce.py