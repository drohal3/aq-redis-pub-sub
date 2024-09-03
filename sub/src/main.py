from dotenv import dotenv_values
from sub import run


ENV_TOPIC = "AQ_REDIS_SUB_TOPIC"
ENV_HOST = "AQ_REDIS_SUB_HOST"
ENV_PORT = "AQ_REDIS_SUB_PORT"

def main():
    env_config = dotenv_values()
    run(
        env_config[ENV_HOST],
        env_config[ENV_PORT],
        env_config[ENV_TOPIC]
    )


if __name__ == '__main__':
    main()

