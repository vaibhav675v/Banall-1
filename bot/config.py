import os

class Config:
    TELEGRAM_TOKEN="5465741754:AAHSsM2FbKQmoB5ZD1uxtpqBTfeab32W9jQ"
    TELEGRAM_APP_HASH="fecaf2028e3d33dc1b6ab77c0361711d"
    TELEGRAM_APP_ID='9004654'
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
