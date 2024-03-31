
from instabot import Bot
import time

def make_request_with_backoff(bot, photo_path, caption):
    max_retries = 3
    retries = 0

    while retries < max_retries:
        try:
            bot.upload_photo(photo_path, caption=caption)
            return
        except Exception as e:
            if "429" in str(e):
                sleep_time = 2 ** retries * 60  # exponential backoff in minutes
                print(f"Rate limit exceeded. Retrying in {sleep_time} seconds.")
                time.sleep(sleep_time)
                retries += 1
            elif "ConnectTimeoutError" in str(e):
                print("Connection timeout error. Retrying...")
                retries += 1
            else:
                print("Error:", e)
                return

    print("Max retries reached. Exiting.")

def main():
    # Instagram credentials
    username = 'TestReelsAws123'
    password = 'Bihar@00714'

    # Photo details
    photo_path = 'picture.jpg'
    caption = 'Hi There'

    # Initialize bot
    bot = Bot()

    # Log in
    bot.login(username=username, password=password)

    # Make request with backoff
    make_request_with_backoff(bot, photo_path, caption)

    # Log out
    bot.logout()

if __name__ == "__main__":
    main()
