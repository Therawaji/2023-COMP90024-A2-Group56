#!/bin/zsh

# 运行上传数据到 main CouchDB 的脚本
#echo "data_twi_mpi start"
#mpiexec -n 4 python3 data_twi_mpi.py
#echo "data_twi_mpi finish"

echo "data_push_external start"
python3 data_push_external.py
echo "data_push_external finish"

# 运行在 twi CouchDB 中做 twi 数据的 mapreduce 的脚本
echo "data_map_reduce start"
python3 data_map_reduce.py
echo "data_map_reduce finish"

# 运行将 twi数据的 mapreduce 的结果上传到 twi CouchDB 的脚本
echo "data_push_mapreduce start"
python3 data_push_mapreduce.py
echo "data_push_mapreduce finish"
