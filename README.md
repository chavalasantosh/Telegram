# Telegram Toolkit

A collection of Python scripts utilizing the Telethon library to automate and manage various tasks on Telegram. This toolkit simplifies processes such as joining channels and classifying Telegram entities into users, channels, and groups based on user dialogs.

## Features

- **Channel Membership Evaluator and Joiner**: Automatically joins Telegram channels from a provided list if the user is not already a member.
- **Telegram Entity Classifier**: Classifies entities into users, channels, and groups based on the dialogs in the user's Telegram account and saves them into separate files.

## Getting Started

### Prerequisites

Before you begin, ensure you have the following requirements installed:
- Python 3.6 or higher
- Telethon library

You can install Telethon using pip:
```bash
pip install telethon
git clone https://github.com/yourusername/telegram-toolkit.git
cd telegram-toolkit
```

Create a .env file or set environment variables for API_ID and API_HASH obtained from my.telegram.org.
Usage
Channel Membership Evaluator and Joiner
Place the list of channel usernames in api/cyberbaby usernames.txt.
Run the script:

```
python join_telegram_channels.py
```

Telegram Entity Classifier
Simply run the script, and it will classify the entities based on your Telegram dialogs:

```
python classify_entities.py
```


## Scripts
join_telegram_channels.py: Joins Telegram channels from a list if not already a member.
classify_entities.py: Fetches dialogs, classifies them into users, channels, and groups, and saves the usernames to respective files.
Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Please refer to the CONTRIBUTING.md for more information.

License
Distributed under the MIT License. See LICENSE for more information.

Acknowledgments
Telethon, a Python 3 MTProto library to interact with Telegram's API as a user or through a bot account.

