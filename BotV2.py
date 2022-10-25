import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import CommandObject
from aiogram import html
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.dispatcher.filters import Text

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="5319086031:AAG7jy0MVHHG50b48VaPHSOvefE_9xN-76A")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
# @dp.message(commands=["start"])
# async def cmd_start(message: types.Message):
#     await message.answer("Здравствуйте! Примите, пожалуйста, участие в опросе, посвященном исследованию оценки удовлетворенности покупкой. Ваши ответы и пожелания помогут исправить имеющиеся ошибки и улучшить качество товаров!")

@dp.message(commands="start")
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Старт")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Начнем"
    )
    await message.answer("Здравствуйте! Примите, пожалуйста, участие в опросе, посвященном исследованию оценки удовлетворенности покупкой. Ваши ответы и пожелания помогут исправить имеющиеся ошибки и улучшить качество товаров!", reply_markup=keyboard)

@dp.message(commands=["name"])
async def cmd_name(message: types.Message, command: CommandObject):
    if command.args:
        await message.answer(f"Привет, {html.bold(html.quote(command.args))}", parse_mode="HTML")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")
# новый импорт!
from aiogram.dispatcher.filters import Text

@dp.message(Text(text="Старт"))
async def cmd_start(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="Да"),
            types.KeyboardButton(text="Нет")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оцените работу интернет магазина"
    )
    await message.answer("Вы делали покупки в нашем интернет магазине?", reply_markup=keyboard)


@dp.message(Text(text="Нет"))
async def with_net(message: types.Message):
    await message.reply("Мы будем рады видеть Вас у себя в магазине, новым покупателям скидка 10%")

@dp.message(lambda message: message.text == "Да")
async def reply_da(message: types.Message):
    builder = ReplyKeyboardBuilder()
    for i in range(1, 10):
        builder.add(types.KeyboardButton(text=str(i)))
    builder.adjust(3)
    await message.answer(
        "Оцените, пожалуйста, купленный Вами товар по 9-балльной шкале, где 1 соответствует очень низкому качеству, 9 – максимально высокому качеству:",
        reply_markup=builder.as_markup(resize_keyboard=True),
    )

@dp.message(lambda message: message.text == "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "8")
async def cmd_size(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Цена должна быть выше за продукт(-ы) такого качества")],
        [types.KeyboardButton(text="Цена соответствует качеству")],
        [types.KeyboardButton(text="Цена должна быть ниже за продукт(-ы) такого качества")]
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="Оцените работу интернет магазина"
    )
    await message.answer("Если говорить о сочетании цены и качества, то как Вы оцените купленный Вами продукт?", reply_markup=keyboard)

@dp.message(Text(text="Цена должна быть выше за продукт(-ы) такого качества"))
async def with_puree(message: types.Message):
    await message.reply("Спасибо, мы рады за ваше доверие")
@dp.message(lambda message: message.text == "Цена соответствует качеству")
async def with_puree(message: types.Message):
    await message.reply("Спасибо, мы рады за ваше доверие")
@dp.message(lambda message: message.text =="Цена должна быть ниже за продукт(-ы) такого качества")
async def with_puree(message: types.Message):
    await message.reply("Спасибо, мы рады за ваше доверие")




# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)



if name == "main":
    asyncio.run(main())