import discord
import random
import json
import os
from datetime import date, datetime, timedelta

# yt video 10:20
path = os.getcwd()
print(path)
os.chdir(path)


# chdir passt sich an, den String Path ändern, wenn du was machen willst

# Helper functions
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

        # reagiert nicht auf eigene Botnachrichten
        if message.author == client.user:
            return

        # Fächer Embeds
        async def etechnik():
            embed_et = discord.Embed(title="Dozent: Chowanetz", colour=discord.Colour(0x9999),
                                     description="Die Vorlesungen werden [hier](https://faubox.rrze.uni-erlangen.de/getlink/fiNUiABo68ky9hWmQLxpF2pU/) aufgezeichnet!\n[Moodlekurs](https://elearning.ohmportal.de/course/view.php?id=3253)```Vorlesungszeiten:\nMontag \t   9.45-11.15  Uhr \nDienstag  \t9.45-11.15  Uhr \nDonnerstag    11.30-13.00 Uhr```")

            embed_et.set_thumbnail(url="https://cdn.discordapp.com/emojis/844547075982622760.png")
            embed_et.set_author(name="Elektrotechnik",
                                url="https://th-nuernberg.zoom.us/j/99486053126?pwd=RGluUW5JY2pWc2xiVTJ4L28zWjNpQT09")

            await message.channel.send(embed=embed_et)

        async def mathe():
            embed_mathe = discord.Embed(title="Dozentin: Rademacher", colour=discord.Colour(0x9999),
                                        description="Die Vorlesungen werden [hier](https://faubox.rrze.uni-erlangen.de/getlink/fiNUiABo68ky9hWmQLxpF2pU/) aufgezeichnet!\n[Moodlekurs](https://elearning.ohmportal.de/course/view.php?id=3253)```Vorlesungszeiten:\nDienstag \t 8.00-9.30  Uhr \nMittwoch  \t9.45-11.15 Uhr \nDonnerstag\t8.00-9.30  Uhr```")

            embed_mathe.set_thumbnail(url="https://cdn.discordapp.com/emojis/844547075982622760.png")
            embed_mathe.set_author(name="Mathe",
                                   url="https://th-nuernberg.zoom.us/j/92451031531?pwd=TU14c2ZsckFVaWVONWppM01YNG9aUT09")
            await message.channel.send(embed=embed_mathe)

        async def physik():
            embed_physik = discord.Embed(title="Dozent: Kottcke", colour=discord.Colour(0x9999),
                                         description="Es wird nicht aufgezeichnet, aber es werden im [Moodlekurs](https://elearning.ohmportal.de/course/view.php?id=9357) die Mitschriften hochgeladen.\n```Vorlesungszeit:\nMontag 11.30-13.00 Uhr```")

            embed_physik.set_thumbnail(url="https://cdn.discordapp.com/emojis/844547075982622760.png")
            embed_physik.set_author(name="Physik",
                                    url="https://th-nuernberg.zoom.us/j/6012092945?pwd=VjNOWStQLzYzcjdGRFRpMnFQTGlmQT09")

            await message.channel.send(embed=embed_physik)

        async def et_uebung():
            embed_et_uebung = discord.Embed(title="Dozent: Pfleger", colour=discord.Colour(0x9999),
                                            description="Es wird nicht aufgezeichnet und nichts hochgeladen.\nLösungsbilder sind im Discord Channel \"et-übung\"\n```Vorlesungszeiten:\nDienstag   11.30-13.00 Uhr\nDonnerstag 14.00-15.30 Uhr\nDonnerstag 15.45-17.15 Uhr```")

            embed_et_uebung.set_thumbnail(url="https://cdn.discordapp.com/emojis/844547075982622760.png")
            embed_et_uebung.set_author(name="ET Übung",
                                       url="https://th-nuernberg.zoom.us/j/91315110443?pwd=Vno0U0pCNlBUM2thWHloQ2RFK1Rudz09")

            await message.channel.send(embed=embed_et_uebung)

        async def mathe_uebung():
            embed_mathe_uebung = discord.Embed(title="Dozentin: Schöning", colour=discord.Colour(0x9999),
                                               description="Es wird nichts aufgezeichnet oder hochgeladen.\nLösungsbilder sind im Discord Channel \"mathe-übung\"\n```Vorlesungszeit:\nMontag   14.10-15.40 Uhr```")

            embed_mathe_uebung.set_thumbnail(url="https://cdn.discordapp.com/emojis/844547075982622760.png")
            embed_mathe_uebung.set_author(name="Mathe Übung",
                                          url="https://th-nuernberg.zoom.us/j/99033427466?pwd=Z1NCa2dzeEtNTm1INi9wZW5JOHFmUT09")

            await message.channel.send(embed=embed_mathe_uebung)

        async def informatik1():
            embed_info = discord.Embed(title="Dozent: Paulus", colour=discord.Colour(0x9999),
                                       description="Es wird nichts aufgezeichnet oder hochgeladen.\nIm [Moodlekurs](https://elearning.ohmportal.de/course/view.php?id=6859) gibt es seine Folien und Videos des letzten Semesters.\n```Vorlesungszeit:\nDonnerstag   9.45-11.15 Uhr```")

            embed_info.set_thumbnail(url="https://cdn.discordapp.com/emojis/844547075982622760.png")
            embed_info.set_author(name="Informatik 1 Vorlesung",
                                  url="https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fteam%2F19%3Aed5f4361d551456cb85f43341b6d23aa%40thread.tacv2%2Fconversations%3FgroupId%3D8e3d7b27-c1d1-4dd9-abd3-27947fe4086e%26tenantId%3Dff180ccd-a30e-43e7-b99c-b9412b24395a&type=team&deeplinkId=a793f997-1a68-4068-8de7-f4f7074f0e90&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")

            await message.channel.send(embed=embed_info)

        async def mathe_tutorium():
            embed_mathte_t = discord.Embed(title="von Larissa", colour=discord.Colour(0x9999),
                                           description="Mitschriften sind in Teams\n```Vorlesungszeit:\nMittwoch   8.00-9.45 Uhr```")

            embed_mathte_t.set_author(name="Mathe Tutorium",
                                      url="https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fchannel%2F19%3A48c9ec6c739d4bdf95894e4951d0c237%40thread.tacv2%2FAllgemein%3FgroupId%3D7d9c6fd6-6d97-44f9-9076-3f93ad5da095%26tenantId%3Dff180ccd-a30e-43e7-b99c-b9412b24395a&type=channel&deeplinkId=51e21896-6373-4705-a270-9f0fce6e7b55&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")

            await message.channel.send(embed=embed_mathte_t)

        async def et_tutorium():
            embed_et_t = discord.Embed(title="von Dominik", colour=discord.Colour(0x9999),
                                       description="```Vorlesungszeit:\nFreitag   8.00-9.45 Uhr```")

            embed_et_t.set_author(name="ET Tutorium",
                                  url="https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fchannel%2F19%3A56aadede9c1b426bbea1b146cd349468%40thread.tacv2%2FAllgemein%3FgroupId%3D0f474a03-379f-4a14-9966-1ef19b5f9a45%26tenantId%3Dff180ccd-a30e-43e7-b99c-b9412b24395a&type=channel&deeplinkId=983cbd58-f252-4c46-9506-f76c0ca8da0e&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true")

            await message.channel.send(embed=embed_et_t)

        # Gibt die Fächerembeds aus, Wenn !Fach "spezielles Fach" eingegeben wird
        if message.content.startswith("!Fach"):
            mes = message.content.split(" ")
            try:
                zusatz = mes[2]
            except IndexError:
                zusatz = " "
            mess = [mes[0].lower(), mes[1].lower(), zusatz.lower()]
            print(mes)
            print(mess)
            if ((mess[1] == "et" or mess[1] == "etechnik" or mess[1] == "elektrotechnik") and mess[2] == " "):
                await etechnik()
            elif mess[1] == "mathe" and mess[2] == " ":
                await mathe()
            elif mess[1] == "physik":
                await physik()
            elif ((mess[1] == "et" or mess[1] == "etechnik" or mess[1] == "elektrotechnik") and mess[2] == "übung"):
                await et_uebung()
            elif (mess[1] == "mathe" and mess[2] == "übung"):
                await mathe_uebung()
            elif ((mess[1] == "et" or mess[1] == "etechnik" or mess[1] == "elektrotechnik") and mess[2] == "tutorium"):
                await et_tutorium()
            elif (mess[1] == "mathe" and mess[2] == "tutorium"):
                await mathe_tutorium()
            else:
                await message.channel.send("Ungültige Eingabe, probiers bitte nochmal")

        # schreibt neue Nachricht mit THATSCRINGE
        if message.content.startswith("!cringe"):
            cringe = ["🇹", "🇭", "🇦", ":t2:841412559726968882", "🇸", "🇨", "🇷", "🇮", "🇳", "🇬", "🇪"]
            await message.delete()
            for i in cringe:
                await message.channel.send(i)
        # gibt die aktuelle Vorlesung mit Link an
        if message.content.startswith("!now"):
            nachricht_zeit = message.created_at.replace(second=0, microsecond=0) + timedelta(hours=2)
            print(nachricht_zeit)
            jetzt = datetime.today().replace(second=0, microsecond=0)
            print(jetzt)
            if (nachricht_zeit == jetzt):
                zeit = nachricht_zeit
                stunde = zeit.hour
                minute = zeit.minute

                # .weekday() 0 = Monday 1 = Tuesday 2 = Wednesday 3 = Thursday 4 = Friday 5 = Saturday 6 = Sunday
                # Unterrichts stunde wird definiert als Unterrichtszeit + 15 min vorher

                # Montag
                if (zeit.weekday() == 0):
                    if (stunde == 7 and minute >= 45 or stunde == 8 or stunde == 9 and minute < 30):  # erste Stunde
                        await message.channel.send("Wir haben jetzt zum Glück frei ")
                    if (stunde == 9 and minute >= 30 or stunde == 10 or stunde == 11 and minute < 15):  # zweite Stunde
                        await etechnik()
                    if (stunde == 11 and minute >= 15 or stunde == 12):  # dritte Stunde
                        await physik()
                    if (stunde == 14 or stunde == 15 and minute <= 30):
                        await mathe_uebung()
                # Dienstag
                elif (zeit.weekday() == 1):
                    if (stunde == 7 and minute >= 45 or stunde == 8 or stunde == 9 and minute < 30):  # erste Stunde
                        await mathe()
                    if (stunde == 9 and minute >= 30 or stunde == 10 or stunde == 11 and minute < 15):  # zweite Stunde
                        await etechnik()
                    if (stunde == 11 and minute >= 15 or stunde == 12):  # dritte Stunde
                        await et_uebung()
                # Mittwoch
                elif (zeit.weekday() == 2):
                    if (stunde == 7 and minute >= 45 or stunde == 8 or stunde == 9 and minute < 30):  # erste Stunde
                        await mathe_tutorium()
                    if (stunde == 9 and minute >= 30 or stunde == 10 or stunde == 11 and minute < 15):  # zweite Stunde
                        await mathe()
                    if (stunde == 11 and minute >= 15 or stunde == 12):  # dritte Stunde
                        await message.channel.send("FREIIIIIIIII!")
                # Donnerstag
                elif (zeit.weekday() == 3):
                    if (stunde == 7 and minute >= 45 or stunde == 8 or stunde == 9 and minute < 30):  # erste Stunde
                        await mathe()
                    if (stunde == 9 and minute >= 30 or stunde == 10 or stunde == 11 and minute < 15):  # zweite Stunde
                        await informatik1()
                    if (stunde == 11 and minute >= 15 or stunde == 12):  # dritte Stunde
                        await etechnik()
                # Freitag
                elif (zeit.weekday() == 4):
                    if (stunde == 7 and minute >= 45 or stunde == 8 or stunde == 9 and minute < 30):  # erste Stunde
                        await et_tutorium()
                    if (stunde == 9 and minute >= 30 or stunde == 10 or stunde == 11 and minute < 15):  # zweite Stunde
                        await message.channel.send("Snens Übungsstunde")
                    if (stunde == 11 and minute >= 15 or stunde == 12):  # dritte Stunde
                        await message.channel.send("Wochenende, SAUFEN")
        if message.content.startswith("!help"):
            embed_help = discord.Embed(colour=discord.Colour(0x9999))

            embed_help.set_author(name="Snensbot Befehle")

            embed_help.add_field(name="!now", value="Gibt die aktuelle Stunde mit Zoomlink und Infos zum Fach zurück",
                                 inline=False)
            embed_help.add_field(name="!Fach \"spezielles Fach\" ", value="Gibt das ausgewählte Fach mit Infos zurück",
                                 inline=False)
            embed_help.add_field(name="reagiere mit :poop:", value="und es wird durch THAT'S CRINGE ersetzt",
                                 inline=False)

            await message.channel.send(embed=embed_help)
        if message.content.startswith("!test"):
            await message.channel.send(
                "https://cdn.discordapp.com/attachments/839789266754076722/845666202709655573/augenkrankheiten-sehschwaechen-simulation-beispielbild-katzenbaby.png")

        # economy part
        if message.content.startswith("!e"):

            mes = message.content.split(" ")
            try:
                zusatz = mes[2]
            except IndexError:
                zusatz = " "
            mess = [mes[0].lower(), mes[1].lower(), zusatz.lower()]

            # Balance

            async def balance(self):
                await open_account(message.author)
                user = message.author
                with open("mainbank.json", "r") as f:
                    users = json.load(f)
                wallet_amt = users[str(message.author.id)]["wallet"]
                bank_amt = users[str(message.author.id)]["bank"]

                em = discord.Embed(title=f"{message.author.name}'s cash", color=39321)
                em.add_field(name="Geldbeutel Balance", value=wallet_amt)
                em.add_field(name="Bank Balance", value=bank_amt)
                await message.channel.send(embed=em)

            # opens Account
            async def open_account(user):
                with open("mainbank.json", "r") as f:
                    users = json.load(f)
                if str(user.id) in users:
                    return False
                else:
                    users[str(user.id)] = {}
                    users[str(user.id)]["wallet"] = 0
                    users[str(user.id)]["bank"] = 0
                    #HIERZU: Entweder 1 und 0 speichern fuer reset um mitternacht, ODER:
                    #Die Zeit speichern und nur nach 6h oder so erlauben, den timer zu ersetzen
                    users[str(user.id)]["paid"] = 0

                # users = await get_bank_data()
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)
                return True

            # async def store_bank_data():

            async def payday(user):
                #payday muss limitert werden, siehe oben
                await open_account(message.author)
                with open("mainbank.json", "r") as f:
                    users = json.load(f)
                earnings = random.randrange(50)
                await message.channel.send(f"An deinem Zahltag kriegst du {earnings} coins")
                users[str(user.id)]["wallet"] += earnings
                with open("mainbank.json", "w") as f:
                    json.dump(users, f)

            if mes[1] == "openaccount":
                await open_account(message.author)
            elif mes[1] == "balance":
                await balance(message.author)
            elif mes[1] == "payday":
                await payday(message.author)

    # Wenn mit :poop: reacted wird, wird es durch THATSCRINGE ersetzt
    async def on_raw_reaction_add(self, payload):
        if (str(payload.emoji) == "💩"):
            user = client.get_user(payload.user_id)
            channel = client.get_channel(payload.channel_id)
            message = await channel.fetch_message(payload.message_id)
            await message.clear_reaction("💩")
            cringe = ["🇹", "🇭", "🇦", ":t2:841412559726968882", "🇸", "🇨", "🇷", "🇮", "🇳", "🇬", "🇪"]
            for i in cringe:
                await message.add_reaction(i)


client = MyClient()
client.run("ODM3NzIwNTAyOTg1NTU1OTk5.YIwqBA.d2jnBMMTOP58V8jMenLLWZBFg9E")
