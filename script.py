from rivescript import RiveScript

bot = RiveScript()
bot.load_directory("./eg/brain")
bot.sort_replies()

while True:
    msg = input('You> ')
    if msg == '/quit':
        quit()
    msg = msg.replace("'", ' ')
    msg = msg.replace("à", 'a')
    msg = msg.replace("ç", 'c')
    msg = msg.replace("é", 'e')
    msg = msg.replace("è", 'e')
    reply = bot.reply("localuser", msg)
    print('Bot>', reply)
