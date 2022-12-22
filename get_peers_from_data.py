import os
import redis
import redis.connection
import sys
import json

def new_redis_conn(db=0):
    """
    Returns new instance of Redis connection with the right db selected.
    """
    socket = os.environ.get('REDIS_SOCKET', None)
    password = os.environ.get('REDIS_PASSWORD', None)
    return redis.StrictRedis(db=db, password=password, unix_socket_path=socket)

# /home/ubuntu/bitnodes/data/crawl/24e92764/1670257174.json
path = sys.argv[1]
f = open(path, 'r')
data = json.load(f)
redis_conn = new_redis_conn(db=0)
for node in data:
    [ip, port, services, height] = node
    print("===================")
    print(ip, ":")
    key = f'peer:{ip}-{port}' #adres - port
    peers = redis_conn.get(key)
    print(peers) # (address, port, services, timestamp)
