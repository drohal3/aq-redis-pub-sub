from redis import Redis

def run(redis_host, redis_port, topic: str):
    print("Subscribing to topic", topic)
    redis = Redis(
        host=redis_host,
        port=redis_port,
        decode_responses=True
    )

    mobile = redis.pubsub()

    try:
        mobile.subscribe(topic)
    except Exception as e:
        print(f"An error occurred: {e}")

    for message in mobile.listen():
        print(message)
