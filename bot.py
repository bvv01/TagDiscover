from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

# API-ключ от BotFather
API_KEY = '7443648123:AAEq3rVm9O4m23u9KjasiDwSWENkn6g8EtA'

# ID администратора (замени на свой Telegram ID)
ADMIN_ID = 222638686  # Получи его через @userinfobot в Telegram

# Функция для обработки команды /start
async def start(update: Update, context: CallbackContext):
    welcome_text = (
        "Hello! I am a bot ready to anonymously receive photos, videos, location points, "
        "and useful information that fits the theme of the website TagDiscover.com.\n\n"
        "If you have a larger submission, you can send it by email to: info@tagdiscover.com.\n\n"
        "Please review our privacy policy here: https://tagdiscover.com/pp-eng."
    )

    follow_up_text = (
        "If you want to share urgent and useful information related to the theme of TagDiscover.com, feel free to send it here."
    )

    await update.message.reply_text(welcome_text)
    await update.message.reply_text(follow_up_text)  # Второе сообщение

# Функция для обработки текстовых сообщений от пользователей
async def handle_message(update: Update, context: CallbackContext):
    text_received = update.message.text
    user_id = update.message.from_user.id  # Получаем ID пользователя

    # Уведомление администратору
    await context.bot.send_message(ADMIN_ID, f"New message from user {user_id}: {text_received}")

    # Ответ пользователю
    await update.message.reply_text("Thank you for your message! We will get back to you shortly.")

# Функция для администратора, чтобы отвечать пользователям
async def admin_reply(update: Update, context: CallbackContext):
    if update.message.from_user.id == ADMIN_ID:  # Проверка, что сообщение от администратора
        args = context.args  # Получаем аргументы команды
        if len(args) < 2:
            await update.message.reply_text("Usage: /admin_reply <user_id> <message>")
            return

        try:
            user_id = int(args[0])  # ID пользователя, которому отвечает администратор
            message_to_send = " ".join(args[1:])  # Сообщение для отправки

            # Отправляем сообщение пользователю
            await context.bot.send_message(user_id, message_to_send)
            await update.message.reply_text(f"Message sent to user {user_id}.")
        except ValueError:
            await update.message.reply_text("Invalid user ID. Please enter a valid number.")

# Основная функция для запуска бота
def main():
    # Создание объекта Application
    application = Application.builder().token(API_KEY).build()

    # Регистрируем обработчики команд
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('admin_reply', admin_reply))

    # Регистрируем обработчик для текстовых сообщений от пользователей
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Запускаем бота
    application.run_polling()
