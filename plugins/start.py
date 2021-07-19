from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["start"]), group=-2)

async def start(client, message):

    # return

    joinButton = InlineKeyboardMarkup([

        [InlineKeyboardButton("Channel", url="https://t.me/PolygonStreetBet")],

        [InlineKeyboardButton(

            "Report Bugs 😊", url="https://t.me/PolygonStreetBet")]

    ])

    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n/📊Download Any YouTube Video.
📊Super First.
📊Bangladeshi Development.
📊Join Support For Help.
📊Use /help For Check How To Use It."

    await message.reply_text(welcomed, reply_markup=joinButton)

    raise StopPropagation

