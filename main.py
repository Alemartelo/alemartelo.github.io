# 0:46 19.07.23 епти
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6349900269:AAG0MUqrjkeF07JEsHSuDRAz3HRaiZInDzw')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://vk.com/audios250287675')))
    await message.answer('qq',reply_markup=markup)










executor.start_polling(dp)


#bot = telebot.TeleBot('6349900269:AAG0MUqrjkeF07JEsHSuDRAz3HRaiZInDzw')
# #bot.infinity_polling()
