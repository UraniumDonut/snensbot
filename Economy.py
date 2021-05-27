import discord
import random
import json
import os
#yt video 10:20
os.chdir("C:\Users\marce\PycharmProjects\DiscordBot\Economy.py")

#Helper functions
async def get_bank_data(self):
    with open("mainbank.json", "r") as f:
        users = json.load(f)
    return users


class MyClient(discord.Client):






    # Einloggen
    async def on_ready(self):
        print("Ich habe mich eingeloggt.")

    # Wenn Nachricht gepostet wird
    async def on_message(self, message):
        if message.author == client.user:
            return

        if message.content.startswith("!e"):
            # Balance
            async def balance(self):
                await open_account(message.author)

                users = await get_bank_data()
                wallet_amt = users[str(message.author.id)]["wallet"]
                bank_amt = users[str(message.author.id)]["bank"]

                em = discord.Embed(title= f"{message.author.name}'s balance", color = 39321 )
                em.add_field(name = "Wallet Balance", value = wallet_amt)
                em.add_field(name="Bank Balance", value=bank_amt)
                await message.channel.send(embed = em)
            # opens Account
            async def open_account(self, user):
                users = await get_bank_data()
                if str(user.id) in users:
                    return False
                else:
                    users[str(user.id)]["wallet"] = 0
                    users[str(user.id)]["bank"] = 0

                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
                return True




client = MyClient()
client.run("ODM3NzIwNTAyOTg1NTU1OTk5.YIwqBA.d2jnBMMTOP58V8jMenLLWZBFg9E")