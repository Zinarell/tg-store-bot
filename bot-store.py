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

global products
products = {
    1:{"name": "iPhone 15", "price": "999"},
    2:{"name": "MacBook Pro", "price": "1999"},
    3:{"name": "AirPods Pro", "price": "249"}
}


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

    async def catalog(self, update:Update, context: ContextTypes, query):
        keyboard = []
        for id in products:
            name = products[id]["name"]
            price = products[id]["price"]
            keyboard += [InlineKeyboardButton(f"{name} - ${price}", callback_data=f"AddBasket {id}")]
        markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("📦 Каталог товаров:",
        reply_markup=markup)


    async def basket(self, update:Update, context: ContextTypes, query):
        keyboard = [
        [InlineKeyboardButton("Оформить заказ", callback_data="make_order")],
    ]
        markup = InlineKeyboardMarkup(keyboard)

        basket_text = ""
        total_price = 0
        k = 1
        for id in context.user_data["basket"]:
            name = products[id]["name"]
            price = products[id]["price"]
            total_price += int(price)
            basket_text += f"{k}. {name} - ${price}\n"
        
        await query.message.reply_text(f"""🛍️ Ваша корзина:
{basket_text}

Итого: ${str(total_price)}""",
reply_markup = markup)


    async def add_product(self, update:Update, context: ContextTypes, query, product_id):
        if context.user_data.get("basket") == None:
            context.user_data["basket"] = []
        else:
            context.user_data["basket"].append(product_id) #Добавляет в корзину не сам продукт, а его id в каталоге
            await query.message.reply_text(f"Товар {products[product_id]["name"]} добавлен в корзину!")

    async def make_order(self, update:Update, context: ContextTypes, query):
        keyboard = [
        [InlineKeyboardButton("Вернуться в каталог", callback_data="catalog")],
    ]
        markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text("Заказ оформлен! Спасибо за покупку!",
        reply_markup = markup)

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data.split()

    await query.message.delete()
    

    commands = {
        "catalog": Commands.catalog,
        "basket": Commands.basket,
        "make_order": Commands.make_order
    }

    if len(data)!= 1:
        if data[0] == "AddBasket":
            Commands.add_product(query, data[1])

    else:
        commands[data[0]](query)



def main():
    builder_app = ApplicationBuilder()#Создаем конфигуратор приложения
    builder_app.token(token=TOKEN)

    app = builder_app.build()#Функция создает бота (ядро приложения)

    print("Бот запущен...")
    app.run_polling()#Начинаем опрашивать телеграмм

main()