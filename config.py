# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28071110")

API_HASH = os.environ.get("API_HASH", "3adf9a220b6debbb23cb8b4a4418d704")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7640881691:AAGFOeF6wmBDv1X4c8bXp1CRrq6lhcQnv5o") 

FORCE_SUB = os.environ.get("FORCE_SUB", "Shashu9148") 

             # Don't Remove Credit @Shashu9148
             # Subscribe YouTube Channel For Amazing Bot @shashu9148
             # Ask Doubt on telegram @ShaNaAdminConnect_Bot

DB_NAME = os.environ.get("DB_NAME", "renamevjbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://shashwathgondi9148:Shashwath@9148@cluster0.edy6amv.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '5606411877').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
