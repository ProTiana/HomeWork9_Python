# Рабочий бот. Реализовано приветствие и вопросы, картинка под вопросом
import asyncio
import fileinput
import logging
from aiogram import Bot, Dispatcher, types

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5520992654:AAHvsvCTKL7a0LOzYhN2adD0vBkcJAlSPLU")
# Диспетчер
dp = Dispatcher(bot)

# Хэндлер на команду /start
@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await message.answer("Hello, my friend! Try command: '/help'!")

# работчик на команду /help
@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await message.reply(
        "Напиши команды:\n"
        "/start - получишь ответ на вопросы обо мне\n"
        "/image - посмотришь картинку\n"
        "/question - задам тебе вопросы \n\n"
        "Перечень вопросов, ответы на которые я знаю:\n"
        "1) Как тебя зовут? 2)Сколько тебе лет? 3) На кого ты учишся?")

# указываем URL на картинку
URL = "https://disk.yandex.ru/i/qntCVQiWa2DvYQ"
# Обработчик на image
@dp.message_handler(commands=["image"])
async def cmd_image(message: types.Message):
    await bot.send_photo(message.from_user.id, URL)

# Создание опроса /question
@dp.message_handler(commands=["question"])
async def poll(message: types.Message):
    await message.answer_poll(question='list = [a, b, c] \nЧто выводит команда: print(list)?',
                              options=['List', 'a, b, c', 'list = [a, b, c]'],
                              type='quiz',
                              correct_option_id=1,
                              is_anonymous=False)
    await message.answer_poll(question='Найди оператор членства',
                              options=['in / not in', 'is / is not', 'не знаю таких'],
                              type='quiz',
                              correct_option_id=0,
                              is_anonymous=False)
    await message.answer_poll(question='Что такое функция map()?',
                              options=['Функция, показывающая адрес расположения объекта',
                                       'Функция, возвращающая итератор  кортежей',
                                       'Функция, которая применяет другую функцию ко всем элементам итерируемого объекта'],
                              type='quiz',
                              correct_option_id=2,
                              is_anonymous=False)


# Обработчик для текстового сообщения - отвечает на вопрос пользователя таким же текстовым сообщением
@dp.message_handler()
async def echo_message(msg: types.Message):
    # await bot.send_message(msg.from_user.id, msg.text)
    # Если введенное сообщение равно "Как тебя зовут?", то отвечаю "Tati"
    if msg.text == "Как тебя зовут?":
        await bot.send_message(msg.from_user.id, "Tati")
    if msg.text == "Сколько тебе лет?":
        await bot.send_message(msg.from_user.id, "Всегда 18)")
    if msg.text == "На кого ты учишься?":
        await bot.send_message(msg.from_user.id, "На программиста)")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
