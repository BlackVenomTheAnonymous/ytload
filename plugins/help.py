from pyrogram import Client, Filters

@Client.on_message(Filters.command(["help"]))

async def start(client, message):

    helptxt = f"How to use the bot? 

🚸Go To "Youtube" Sharch Any Video.
🚸Drop The YouTube Video Link Here.
🚸Easy Download.
🚸 Owner : @GodFatherMob

"Please support the Bangladeshi Developers For More Bot""

    await message.reply_text(helptxt)

