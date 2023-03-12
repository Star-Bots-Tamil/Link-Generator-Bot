from pyrogram import filters

################################################################################################################################################################################################################################################
# Supports of Telegram Files 📂 Type

def ns_filter(_,__,message):
   if str(message.text)[1:6] == "start":
     if str(message.text)[7:].lower() == "files_list":
       return True
     else:
       return False
   else:
      return False

files_list_filter = filters.create(ns_filter)
