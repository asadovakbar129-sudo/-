import telebot # Импортируем библиотеку pyTelegramBotAPI

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота, полученный от BotFather
TOKEN = '8804367208:AAGq8v-jaumsNoPkEICKWtTaQUh8KST9Tok' 
bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Отправляем приветственное сообщение
    bot.reply_to(message, "Привет, я твой ИИ-помощник! Чтобы начать пользоваться, перейди в мини-приложение.")

# Запускаем бота
bot.infinity_polling()
