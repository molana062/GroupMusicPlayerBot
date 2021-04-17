from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Alo Jomblo, Ini {bn} 🎵

Jomblo mau denger musik? Bisa tenang aja. Manage by [Mol](https://t.me/Betterthaanhecan).

Ya kalo putus-putus wajarin aja kaya hubungan lu tuh ehe!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👿Syntyche", url="https://t.me/syntychegroup")
                  ],[
                    InlineKeyboardButton(
                        "⚜Channel", url="https://t.me/ruangpublikk"
                    ),
                    InlineKeyboardButton(
                        "Mol", url="https://t.me/Betterthaanhecan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Jomblo Lu", url="https://t.me/Leviousas"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👿 Join sini!", url="https://t.me/syntychegroup")
                ]
            ]
        )
   )


