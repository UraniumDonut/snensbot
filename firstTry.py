import discord

class MyClient(discord.Client):
    #Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")

    #Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("hello bot"):
            await message.channel.send('Hello!')
            await message.author.send("Du hast mich kontaktiert")
        elif message.content.startswith("stats"):
            messages = await message.channel.history(limit=50).flatten()
            for i in messages:
                print(i.content)
            counter = 0
            async for m in message.channel.history():
                if m.author == client.user and m.content == "Leider verloren :(":
                    counter = counter + 1
            print (counter)
        else:
            await message.add_reaction()
    async def on_typing(self, channel, user, when):
        return
        #print(str(user) + " tippt gerade in " + str(channel) + " channel seit " + str(when))
    async def on_message_delete(self, message):
        print("Gelöschte Nachricht: "+ message.content)
client = MyClient()
client.run("ODM3NzIwNTAyOTg1NTU1OTk5.YIwqBA.d2jnBMMTOP58V8jMenLLWZBFg9E")