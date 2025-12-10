from telegram  import (Update, 
                        ReplyKeyboardMarkup, 
                        ReplyKeyboardRemove,
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


def main():
    builder_app = ApplicationBuilder()#Создаем конфигуратор приложения
    builder_app.token(token=TOKEN)

    app = builder_app.build()#Функция создает бота (ядро приложения)

    print("Бот запущен...")
    app.run_polling()#Начинаем опрашивать телеграмм

main()