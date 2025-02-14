from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Вставь сюда свой API-ключ, полученный от BotFather
API_KEY = '7443648123:AAEq3rVm9O4m23u9KjasiDwSWENkn6g8EtA'

# Функция обработчика команды /start
async def start(update: Update, context: CallbackContext):
    # Сообщение, которое будет отправлено пользователю при вызове команды /start
    await update.message.reply_text('Привет! Я ваш новый бот.')

def main():
    # Создаем объект Application и передаем API-ключ
    application = Application.builder().token(API_KEY).build()

    # Регистрируем обработчик для команды /start
    application.add_handler(CommandHandler('start', start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
