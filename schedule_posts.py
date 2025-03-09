import schedule
import time
from instabot import Bot

def post_video():
    bot = Bot()
    bot.login(username="stynraey", password="Hollycrapps.1#")
    bot.upload_video("final_video.mp4", caption="Check out this weird money fact!")

# Schedule the post every day at 10 AM
schedule.every().day.at("10:00").do(post_video)

# Keep the script running
while True:
    schedule.run_pending()
    time.sleep(1)
