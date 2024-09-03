from redis import Redis
import json

def main():
    redis_host = "127.0.0.1"
    redis_port = 6379
    data = {"data": "just testing"}
    redis = Redis(host=redis_host, port=redis_port, decode_responses=True)
    redis.publish("aq_data", json.dumps(data))


if __name__ == '__main__':
    main()

