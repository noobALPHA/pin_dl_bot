from plugs.pin import download
from plugs.texts import caption, error, waiting_text
from pyrogram import Client, filters
from pyrogram.types import Message


@Client.on_message(
    filters.regex(r"(pinterest\.com/pin/[^/]+|pin\.it/[^/]+)(/$|$)")
)
async def pin_dl(client, msg: Message) -> Message:
    url = f"https://{msg.matches[0].group(1)}"
    msg_tmp: Message = await msg.reply_text(waiting_text, quote=True)
    
    dl = download(url)
    if dl:
        send_type, url = dl
        await msg_tmp.edit_text("**__Uploading to telegram__**")
        if send_type == "gif":
            await client.send_animation(msg.chat.id, animation=url, caption=caption, reply_to_message_id=msg.message_id)
        
        elif send_type == "video":
            await client.send_video(msg.chat.id, video=url, caption=caption, reply_to_message_id=msg.message_id)
        
        elif send_type == "image":
            await client.send_photo(msg.chat.id, photo=url, caption=caption, reply_to_message_id=msg.message_id)
        
        await msg_tmp.delete()
            
    else:
        await msg.reply_text(error)


@Client.on_edited_message(
    filters.regex(r"(pinterest\.com/pin/[^/]+|pin\.it/[^/]+)(/$|$)")
)
async def pin_dl_edited(client, msg: Message) -> Message:
    url = f"https://{msg.matches[0].group(1)}"
    msg_tmp: Message = await msg.reply_text(waiting_text, quote=True)
    
    dl = download(url)
    if dl:
        send_type, url = dl
        await msg_tmp.edit_text("**__Uploading to telegram__**")
        if send_type == "gif":
            await client.send_animation(msg.chat.id, animation=url, caption=caption, reply_to_message_id=msg.message_id)
        
        elif send_type == "video":
            await client.send_video(msg.chat.id, video=url, caption=caption, reply_to_message_id=msg.message_id)
        
        elif send_type == "image":
            await client.send_photo(msg.chat.id, photo=url, caption=caption, reply_to_message_id=msg.message_id)
        
        await msg_tmp.delete()
            
    else:
        await msg.reply_text(error)
