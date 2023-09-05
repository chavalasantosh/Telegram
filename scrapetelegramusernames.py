from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import Channel, Chat, User, InputPeerUser, InputPeerChannel, InputPeerChat
import asyncio

api_id = '12345678'
api_hash = 'hash'
session_name = 'mysession'

usernames_all = []
chunk_size = 200

usernames = []
groups = []
channels_list = []

async def classify_entity(client, entity_name):
    try:
        entity = await client.get_input_entity(entity_name)
        if isinstance(entity, InputPeerUser):
            usernames.append(entity_name)
        elif isinstance(entity, InputPeerChannel):
            channels_list.append(entity_name)
        elif isinstance(entity, InputPeerChat):
            groups.append(entity_name)
    except Exception as e:
        print(f"Error with {entity_name}: {e}")

async def main():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        if not await client.is_user_authorized():
            await client.start()

        last_date = None  # Move the definition here

        while True:
            all_dialogs = await client(GetDialogsRequest(
                offset_date=last_date,
                offset_id=0,
                offset_peer=await client.get_input_entity('me'),
                limit=chunk_size,
                hash=0
            ))

            if not all_dialogs.chats:
                break

            for entity in all_dialogs.chats:
                if isinstance(entity, Channel) and entity.username:
                    usernames_all.append("@" + entity.username if not entity.username.startswith("@") else entity.username)

            for entity in all_dialogs.users:
                if isinstance(entity, User) and entity.username:
                    usernames_all.append("@" + entity.username if not entity.username.startswith("@") else entity.username)

            if all_dialogs.messages:
                valid_dates = [msg.date for msg in all_dialogs.messages if msg.date is not None]
                if valid_dates:
                    last_date = min(valid_dates)


        tasks = [classify_entity(client, e) for e in usernames_all]
        await asyncio.gather(*tasks)

        # Saving results to separate files
        with open('profiles.txt', 'w') as f:
            for u in usernames:
                f.write(u + '\n')

        with open('channels.txt', 'w') as f:
            for c in channels_list:
                f.write(c + '\n')

        with open('groups.txt', 'w') as f:
            for g in groups:
                f.write(g + '\n')

        print("Usernames saved in profiles.txt")
        print("Channels saved in channels.txt")
        print("Groups saved in groups.txt")

asyncio.run(main())
