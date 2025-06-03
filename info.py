import re
import os
from os import environ
from pyrogram import enums
from Script import script
import asyncio
import json
from collections import defaultdict
from pyrogram import Client

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

#main variables
API_ID = int(environ.get('API_ID', '21134445'))
API_HASH = environ.get('API_HASH', '231c18ea7273824491d6bf05425ab74e')
BOT_TOKEN = environ.get('BOT_TOKEN', '')
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '7763229951').split()]
USERNAME = environ.get('USERNAME', 'https://telegram.me/THEHYPER_ACX')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ' -1002334193967'))
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002367446556').split()]
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Thehyper1232:jszZTsxI9MMLE9ut@cluster0.yscc74b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_URI2 = environ.get('DATABASE_URI2', "mongodb+srv://sungjunwoo1232:eRJgnE50iqnURK1n@cluster0.t0zsw5i.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = environ.get('DATABASE_NAME', "Hyper")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Hyper')
LOG_API_CHANNEL = int(environ.get('LOG_API_CHANNEL', ' -1002334193967'))
QR_CODE = environ.get('QR_CODE', 'https://files.catbox.moe/addn2n.jpg')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]

#this vars is for when heroku or koyeb acc get banned, then change this vars as your file to link bot name
BIN_CHANNEL = int(environ.get('BIN_CHANNEL', '0'))
URL = environ.get('URL', 'https://damp-goldarina-acxbots-773c6e78.koyeb.app/')

# verify system vars
IS_VERIFY = is_enabled('IS_VERIFY', True)
LOG_VR_CHANNEL = int(environ.get('LOG_VR_CHANNEL', '-1002476467166'))
TUTORIAL = environ.get("TUTORIAL", "https://t.me/howtoopen_modijiurls/19")
TUTORIAL2 = environ.get("TUTORIAL2", "https://t.me/howtoopen_modijiurls/19")
TUTORIAL3 = environ.get("TUTORIAL3", "https://t.me/howtoopen_modijiurls/19")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/45a270fc6a0a1c183c614.jpg")
SHORTENER_API = environ.get("SHORTENER_API", "e93099db2b7ff5295aa88399c17a50ba72ff3690")
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "shortner.in")
SHORTENER_API2 = environ.get("SHORTENER_API2", "e93099db2b7ff5295aa88399c17a50ba72ff3690")
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "shortner.in")
SHORTENER_API3 = environ.get("SHORTENER_API3", "e93099db2b7ff5295aa88399c17a50ba72ff3690")
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "shortner.in")
TWO_VERIFY_GAP = int(environ.get('TWO_VERIFY_GAP', "3600"))
THREE_VERIFY_GAP = int(environ.get('THREE_VERIFY_GAP', "21600"))

# languages search
LANGUAGES = ["hindi", "english", "telugu", "tamil", "kannada", "malayalam"]

auth_channel = environ.get('AUTH_CHANNEL', '-1002348758566 -1002326594935 -1002107236622')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
SUPPORT_GROUP = int(environ.get('SUPPORT_GROUP', '-1002504526170'))

# bot settings
AUTO_FILTER = is_enabled('AUTO_FILTER', True)
PORT = os.environ.get('PORT', '8080')
MAX_BTN = int(environ.get('MAX_BTN', '8'))
AUTO_DELETE = is_enabled('AUTO_DELETE', True)
DELETE_TIME = int(environ.get('DELETE_TIME', 600))
IMDB = is_enabled('IMDB', False)
FILE_CAPTION = environ.get('FILE_CAPTION', f'{script.FILE_CAPTION}')
IMDB_TEMPLATE = environ.get('IMDB_TEMPLATE', f'{script.IMDB_TEMPLATE_TXT}')
LONG_IMDB_DESCRIPTION = is_enabled('LONG_IMDB_DESCRIPTION', False)
PROTECT_CONTENT = is_enabled('PROTECT_CONTENT', True)
SPELL_CHECK = is_enabled('SPELL_CHECK', True)
LINK_MODE = is_enabled('LINK_MODE', True)
PM_SEARCH = is_enabled('PM_SEARCH', False)
