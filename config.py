import os



class Config(object):
      BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7675882405:AAGVI3Ar6YMgss7NsVnuvVJoQGNEzfUaaZU")
      API_ID = int(os.environ.get("APP_ID", 23621595))
      API_HASH = os.environ.get("API_HASH", 'de904be2b4cd4efe2ea728ded17ca77d')
      CAPTION_POSITION = os.environ.get("CAPTION_POSITION", "nil")
      ADMIN_USERNAME = os.environ.get("ADMIN_USERNAME", "botmaster55")
      ADMIN_ID = int(os.environ.get("ADMIN_ID", 1249672673 )) 
      # DB_URL = os.environ.get("DATABASE_URL", "mongodb+srv://mongodb011:rxXV4pGzxLJgxaXQ@cluster0.undjh.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
