from environs import Env

env = Env()
env.read_env()

NODE_URL = env('NODE_URL', default = 'https://node1.testnet.pokt.network')