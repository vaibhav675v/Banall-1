import os

class Config:
    TELEGRAM_TOKEN="5422231437:AAEqfUE-LooFl3ER3FARYOlGJ8AjwCaxAWE"
    TELEGRAM_APP_HASH="7fb84143bb5f12156dc1835355d4e70e"
    TELEGRAM_APP_ID='10897780'
    
    if not TELEGRAM_TOKEN:
        raise ValueError('TELEGRAM BOT TOKEN not set')
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
