import asyncio
import time

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message

token = ""

bot = Bot(token=token)
dp = Dispatcher(bot)

NameBot = "@MenuBMbot"

start_buttons = ["Меню"]
keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(*start_buttons)


class parametrs():
    last_message = time.time()
    Works = 1


@dp.message_handler(commands="start")
async def start(message: Message):
    if message.chat.id == message.from_user.id:
        button_check = InlineKeyboardButton(text='Связанные Группы', callback_data='group')
        button_sprav = InlineKeyboardButton(text='Справочники', callback_data='sprav')
        button_urls = InlineKeyboardButton(text='Интернет ссылки', callback_data='urls')
        keyboard = InlineKeyboardMarkup(row_width=1).add(button_check, button_sprav, button_urls)
        a = await message.answer("Пожалуйста выбирите из списка ниже", reply_markup=keyboard)
        await asyncio.sleep(400)
        await a.delete()
        await message.delete()
    else:
        if message.chat.id == message.from_user.id:
            start_buttons = ["Меню"]
            keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)
            await message.answer("Приветствую выбери нужное из списка ниже", reply_markup=keyboard)
        else:
            answer = await bot.get_chat_member(message.chat.id, message.from_user.id)
            print(answer)
            if answer.status == "administrator" or answer.status == "creator":
                button_check = InlineKeyboardButton(text='Меню', url="https://t.me/MenuBMbot")
                keyboard = InlineKeyboardMarkup().add(button_check)
                await message.delete()
                a = await message.answer("Меню", reply_markup=keyboard, disable_notification=True)
                await a.pin(disable_notification=True)
            else:
                await message.delete()


@dp.message_handler(Text(equals="Меню"))
async def check(message: types.Message):
    if message.chat.id == message.from_user.id:
        button_check = InlineKeyboardButton(text='Связанные Группы', callback_data='group')
        button_sprav = InlineKeyboardButton(text='Справочники', callback_data='sprav')
        button_urls = InlineKeyboardButton(text='Интернет ссылки', callback_data='urls')
        keyboard = InlineKeyboardMarkup(row_width=1).add(button_check, button_sprav, button_urls)
        a = await message.answer("Пожалуйста выбирите из списка ниже", reply_markup=keyboard)
        await asyncio.sleep(400)
        await a.delete()
        await message.delete()
    else:
        await message.delete()


@dp.callback_query_handler(Text(startswith="menu"))
async def check(callback: types.CallbackQuery):
    await callback.answer()
    button_check = InlineKeyboardButton(text='Группы', callback_data='group')
    button_sprav = InlineKeyboardButton(text='Справочники', callback_data='sprav')
    button_urls = InlineKeyboardButton(text='Интернет ссылки', callback_data='urls')
    keyboard = InlineKeyboardMarkup(row_width=1).add(button_check, button_sprav, button_urls)
    await callback.message.edit_text("Пожалуйста выбирите из списка ниже", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="group"))
async def check(callback: types.CallbackQuery):
    await callback.answer()
    button_sosed = InlineKeyboardButton(text='Соседи', url="https://t.me/+RC6ZqGKW05I2NGM6")
    button_avto = InlineKeyboardButton(text='Автобус', url="https://t.me/+Boh3DbtJH_41NGRi")
    button_stroi = InlineKeyboardButton(text='Строительство', url="https://t.me/+36Qg80j0nk5jMzli")
    button_gaz = InlineKeyboardButton(text='Газификация', url="https://t.me/+M0mUu0WG3c5kMTAy")
    button_back = InlineKeyboardButton(text='Назад', callback_data='menu')
    keyboard = InlineKeyboardMarkup(row_width=1).add(button_sosed, button_avto, button_stroi, button_gaz, button_back)
    await callback.message.edit_text("Пожалуйста выбирите из списка ниже", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="sprav"))
async def check(callback: types.CallbackQuery):
    await callback.answer()
    button_sosed = InlineKeyboardButton(text='Справочник', url="https://vk.com/@bolmos-spravochnye-telefony")
    button_avto = InlineKeyboardButton(text='Расписание автобусов',
                                       url="https://vk.com/@bolmos-raspisanie-obschestvennogo-transporta")
    button_stroi = InlineKeyboardButton(text='Поиск контактов', url="https://t.me/TelefonBMbot")
    button_back = InlineKeyboardButton(text='Назад', callback_data='menu')
    keyboard = InlineKeyboardMarkup(row_width=1).add(button_sosed, button_avto, button_stroi, button_back)
    await callback.message.edit_text("Пожалуйста выбирите из списка ниже", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="urls"))
async def check(callback: types.CallbackQuery):
    await callback.answer()
    button_sosed = InlineKeyboardButton(text='ВК-Б.Мось', url="https://vk.com/bolmos")
    button_avto = InlineKeyboardButton(text='ВК-Подслушано', url="https://vk.com/martyanovomospazderino")
    button_stroi = InlineKeyboardButton(text='МОО ТОС «Б.Мось»', url="https://bol-mos.ru/")
    button_back = InlineKeyboardButton(text='Назад', callback_data='menu')
    keyboard = InlineKeyboardMarkup(row_width=1).add(button_sosed, button_avto, button_stroi, button_back)
    await callback.message.edit_text("Пожалуйста выбирите из списка ниже", reply_markup=keyboard)


@dp.callback_query_handler(Text(startswith="check"))
async def check(callback: types.CallbackQuery):
    await callback.answer()
    print(callback)
    message = callback.message
    answer = await bot.get_chat_member(message.chat.id, callback.from_user.id)
    if answer.status == "creator":
        answer = await bot.get_chat_member(message.chat.id, message.from_user.id)
        if answer.status == "administrator":
            if answer.can_pin_messages:
                button_check = InlineKeyboardButton(text='Меню', url="https://t.me/MenuBMbot")
                keyboard = InlineKeyboardMarkup().add(button_check)
                await message.delete()
                await message.answer("Меню", reply_markup=keyboard, disable_notification=True)
        else:
            button_check = InlineKeyboardButton(text='Проверить', callback_data='check')
            keyboard = InlineKeyboardMarkup().add(button_check)
            await message.edit_text("Права администратора не выданны", reply_markup=keyboard)


@dp.message_handler(content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_members_handler(message: Message):
    if message.new_chat_members[0].id == 5607503801:
        button_check = InlineKeyboardButton(text='Проверить', callback_data='check')
        keyboard = InlineKeyboardMarkup().add(button_check)
        await message.answer("Приветствую для продолжения использования бота, нужно выдать мне права администратора:)",
                             reply_markup=keyboard, disable_notification=True)


@dp.message_handler(content_types=types.ContentType.PINNED_MESSAGE)
async def pined_handler(message: Message):
    if message.from_user.id == 5607503801:
        pass
    else:
        button_check = InlineKeyboardButton(text='Меню', url="https://t.me/MenuBMbot")
        keyboard = InlineKeyboardMarkup().add(button_check)
        text = f"{message.pinned_message.from_user.mention}:\n {message.pinned_message.text}"
        if message.pinned_message.text != None:
            a = await bot.send_message(chat_id=message.pinned_message.chat.id,
                                       text=text, reply_markup=keyboard)
            await message.pinned_message.delete()
            await a.pin()
        elif message.pinned_message.photo != []:
            a = await bot.send_photo(chat_id=message.chat.id, photo=message.pinned_message.photo[0].file_id,
                                     caption=message.pinned_message.caption, reply_markup=keyboard)
            s = await a.pin()
            await message.pinned_message.delete()
        # await message.delete()


@dp.message_handler(state="*", content_types=types.ContentType.all())
async def all(message: Message):
    print(message)


executor.start_polling(dp, skip_updates=False)
