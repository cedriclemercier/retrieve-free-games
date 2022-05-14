import os
from datetime import date

from decouple import config
from discord import Webhook, RequestsWebhookAdapter
from requests_html import HTMLSession, AsyncHTMLSession

WEBHOOK = os.environ.get('WEBHOOK', config('WEBHOOK'))
URL_PCGAMER = os.environ.get('URL_PCGAMER', config('URL_PCGAMER'))

asession = AsyncHTMLSession()

def send_to_discord(message):
    """Send the data to discord webhook

    Args:
        data: the text data to send
    """
    webhook = Webhook.from_url(WEBHOOK, adapter=RequestsWebhookAdapter())
    webhook.send(message)
    

def format_for_discord(title, gamelist):
    message = title + " @everyone \n ============== \n"
    
    for game in gamelist:
        message += f'{game[0]} \n {game[1]} \n ----- \n'
        
    return message
     


async def get_pcgamer():
    r = await asession.get(URL_PCGAMER)
    
    try:
        article = r.html.find('#article-body', first=True)
        title = article.find('h2')[1].text
        
        free_games = article.find('a')[4:]
        
        game_list = []
        
        for game in free_games:
            gametitle = game.text
            link = game.attrs["href"]
            game_list.append((gametitle, link))
            
        print(f'Found {len(game_list)} free games')
    except:
        print(f"Issue retreving data from {URL_PCGAMER}")
        
    
    try:
        print("Sending to discord..")
        message = format_for_discord(title, game_list)
        send_to_discord(message)
    except:
        print("Issue sending to discord")
    

# ============================================

def get_sessions():
    a = asession.run(get_pcgamer)
    
def main():
    get_sessions()
        

if __name__ == "__main__":
    main()