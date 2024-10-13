import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7084999554:AAGpuliYzeu-jDcigEs7O5xHJwHWLqiekkQ")
      API_ID = int(os.environ.get("APP_ID", 21179966))
      API_HASH = os.environ.get("API_HASH", 'd97919fb0a3c725e8bb2a25bbb37d57c')
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "Scammer_botxz")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 7326397503 )) 
      # DB_URL = os.environ.get("DATABASE_URL", "")
