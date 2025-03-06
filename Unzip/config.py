import os

class Config(object):
     
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7477724125:AAEQBrDHbxbfxgnzBusNTaZvLZ_vunT28GA")
    API_ID = int(os.environ.get("API_ID", 29025963))
    API_HASH = os.environ.get("API_HASH", "c6e5ae97263b00062c72f13649f325a4")
