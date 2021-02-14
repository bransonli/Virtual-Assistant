import sqlite3
import commands
from conversational import virtual_assistant as va 

db = sqlite3.connect('commands.db')

cursor = db.cursor()

Command_number = []
Keyword = []
Command = []

cursor.execute('''SELECT command FROM Voice_commands''')
command = cursor.fetchall()

for item in command:
    item = str(item)
    item = item.replace(",)", "")
    item = item.replace("(", "")
    item = item.replace("'", "")
    Command.append(item)

cursor.execute('''SELECT keyword FROM Voice_commands''')
keyword = cursor.fetchall()

for item in keyword:
    item = str(item)
    item = item.replace(",)", "")
    item = item.replace("(", "")
    item = item.replace("'", "")
    Keyword.append(item)

cursor.execute('''SELECT command_number FROM Voice_commands''')
command_number = cursor.fetchall()

for item in command_number:
    item = str(item)
    item = item.replace(",)", "")
    item = item.replace("(", "")
    item = item.replace("'", "")
    Command_number.append(item)

'''
call = getattr(commands,'firefox')
call()
'''

def check_database(dialogue):
    print("done listening")
    for word in Keyword:
        if word in dialogue:
            call = getattr(commands,word)
            return True
        else:
            return False

check_database(va.convert())