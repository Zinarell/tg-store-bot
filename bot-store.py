from telegram  import (Update, 
                        ReplyKeyboardMarkup, 
                        ReplyKeyboardRemove,
                        InlineKeyboardButton,
                        InlineKeyboardMarkup
                        )
from telegram.ext import ( ApplicationBuilder,
                            CommandHandler,
                            ContextTypes,
                            MessageHandler,
                            filters,
                            ConversationHandler
                            )

import random as r
import dotenv
import os
dotenv.load_dotenv()
TOKEN = os.getenv("TOKEN")



class Commands:
    def __init__(self, app):
        start_handler = CommandHandler("start",self.start)
        app.add_handler(start_handler)

    async def start(self, update:Update, context: ContextTypes):
        keyboard = [
        [InlineKeyboardButton("Каталог 🛒", callback_data="catalog")],
        [InlineKeyboardButton("Корзина 🛍️", callback_data="basket")],
    ]
        markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text("Добро пожаловать в магазин! Выберите действие:",
        reply_markup=markup)


def main():
    builder_app = ApplicationBuilder()#Создаем конфигуратор приложения
    builder_app.token(token=TOKEN)

    app = builder_app.build()#Функция создает бота (ядро приложения)

    print("Бот запущен...")
    app.run_polling()#Начинаем опрашивать телеграмм

main()