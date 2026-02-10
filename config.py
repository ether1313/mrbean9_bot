import os
from dotenv import load_dotenv

load_dotenv()

# Bot Token (from environment variables)
BOT_TOKEN = os.getenv("BOT_TOKEN", "8403036424:AAEo7da6FiJqCjfLozEufK3116Irh1NvBy0")

# Channel and link configuration
TELEGRAM_CHANNEL = os.getenv("TELEGRAM_CHANNEL", "https://t.me/Mrbean9a")
FREE_SPIN_URL = os.getenv("FREE_SPIN_URL", "https://mrbean9.com/RFMRBEAN9BOT")
FREE_CREDIT_URL = os.getenv("FREE_CREDIT_URL", "https://mrbean9.com/RFMRBEAN9BOT")

# Promotional images (local file paths - hardcoded in code)
FREE_SPIN_IMAGE_PATH = "public/free_spin.jpg"
HOT_GAME_TIPS_IMAGE_PATH = "public/hot_game_tips.jpg"

# Bot information
BOT_NAME = "Mrbean9 Promo Bot"
BOT_DESCRIPTION = "Mrbean9 Marketing Assistant - Provides latest promotions and event information"
