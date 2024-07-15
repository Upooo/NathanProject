from NP import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Handler untuk perintah /bchannel
@app.on_message(filters.command("bchannel") & filters.private)
async def broadcast_command(client, message):
    try:
        # Ekstrak teks perintah setelah /bchannel
        command_text = message.text.split(" ", 1)[1]
        
        # Pisahkan parameter menggunakan "-"
        parts = command_text.split(" - ")
        
        # Ekstrak parameter
        channel_username = parts[0].strip()
        text = parts[1].strip()
        buttons = []
        
        if len(parts) > 2:
            for part in parts[2:]:
                if part.startswith("button"):
                    button_parts = part.split(", ")
                    button_name = button_parts[0].split(":")[1].strip()
                    button_url = button_parts[1].split(":")[1].strip()
                    buttons.append([InlineKeyboardButton(button_name, url=button_url)])
        
        # Buat markup tombol jika ada tombol
        reply_markup = None
        if buttons:
            reply_markup = InlineKeyboardMarkup(buttons)
        
        # Kirim pesan ke saluran
        await app.send_message(chat_id=channel_username, text=text, reply_markup=reply_markup)
        
        await message.reply_text("Pesan berhasil disiarkan ke saluran.")
    except Exception as e:
        await message.reply_text(str(e))
