import redis
from redis import StrictRedis

# Redis server configuration
redis_host = 'localhost'
redis_port = 6379

# Create a Redis client
redis_client = redis.StrictRedis(host=redis_host, port=redis_port)

try:
    # Test the connection
    response = redis_client.ping()
    print("Connection to Redis successful:", response)
except redis.ConnectionError as e:
    print("Unable to connect to Redis:", e)
