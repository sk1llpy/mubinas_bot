import environs

environs.load_dotenv()
env = environs.Env()

BOT_TOKEN = env.str("TOKEN")
ADMIN = env.int("ADMIN")