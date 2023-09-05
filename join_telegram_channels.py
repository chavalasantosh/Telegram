
import asyncio
from telethon import TelegramClient, functions, errors, types
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantSelf

# Function to read the usernames from the file
def get_channels_from_file(filename='api/cyberbaby usernames.txt'):
    with open(filename, 'r') as file:
        # Read each line, strip it, and return as a list
        return [line.strip() for line in file.readlines()]

# Get channels from the file
channels = get_channels_from_file()

api_id = 24227251
api_hash = '6f4256071365e1790796e48f5275e0ff'
session_name = 'my_session'

client = TelegramClient(session_name, api_id, api_hash)

async def is_member_of_channel(channel):
    try:
        entity = await client.get_input_entity(channel)
        
        if not isinstance(entity, (types.InputPeerChannel, types.InputPeerChat)):
            print(f"{channel} is not a channel or supergroup. Skipping.")
            return True

        me = await client.get_me()
        # Try to get participant details for the current user
        participant = await client(GetParticipantRequest(channel=entity, participant=types.InputPeerUser(user_id=me.id, access_hash=me.access_hash)))
        # If the code reaches this line, you're a participant. Otherwise, UserNotParticipantError is raised.
        return isinstance(participant.participant, ChannelParticipantSelf)
        
    except errors.UserNotParticipantError:
        return False
    except (errors.UsernameInvalidError, errors.UsernameNotOccupiedError):
        print(f"Invalid or unoccupied username: {channel}")
        return True  # Returning True to skip this channel
    except ValueError:
        print(f"No user has '{channel}' as username. Skipping.")
        return True  # Returning True to skip this channel


async def join_channel(channel):
    if await is_member_of_channel(channel):
        print(f"Already a member of {channel}")
        return

    try:
        await client(functions.channels.JoinChannelRequest(channel=channel))
        print(f"Successfully joined channel: {channel}")
    except Exception as e:
        print(f"Failed to join channel: {channel}. Error: {e}")
        await asyncio.sleep(5)

async def main():
    await client.start()
    tasks = [join_channel(channel) for channel in channels]
    await asyncio.gather(*tasks)
    await client.disconnect()

# Run the main coroutine
asyncio.run(main())
