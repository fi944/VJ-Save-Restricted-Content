import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6360586342:AAG3Lze43MbAVzwaZogeu_Nu4YRjApne-eU")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "10122221"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0599f028e8b0e5ac86dc36cbe32d87d8")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "881535564"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://mihaja5084:yeIh95RrMkRNZ3It@cluster0 .6voc3fm.mongodb.net/?retryWrites=true&w=majority") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
