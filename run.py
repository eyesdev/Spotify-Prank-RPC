# libraries
import json
from pypresence import Presence
from colorama import Fore
import time

# read config
def read_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config


# update rpc
def update_rpc():
    config = read_config()
    
    client_id = config.get('client_id', 'YOUR_CLIENT_ID')
    bot_token = config.get('bot_token', 'YOUR_BOT_TOKEN')
    RPC = Presence(client_id, bot_token=bot_token)
    RPC.connect()

    details = config.get('song_name', 'Listening to Spotify')
    state = config.get('song_artist', 'Unknown Artist')
    image = config.get('image', 'default')
    link = config.get('link', '')

    if link:
        buttons = [{
            'label': 'Listen',
            'url': link
        }]
    else:
        buttons = []

    RPC.update(
        details=details,
        state=state,
        large_image=image,
        buttons=buttons
    )

# actually update the rpc
if __name__ == '__main__':
    print(Fore.GREEN + "[+]", Fore.BLUE + "Loading RPC...")
    time.sleep(1)
    update_rpc()
    print(Fore.GREEN + "[+]", Fore.BLUE + "Loaded RPC!")
