from bot import Souris
import config
import asyncio

def run_bot():
	loop = asyncio.get_event_loop() 
	bot = Souris()
	bot.run()
	
	
if __name__ == '__main__':
	run_bot()
