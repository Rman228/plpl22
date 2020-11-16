import telebot
from emoji import emojize
import redis
from redis import StrictRedis

r = redis.from_url(
    'redis://h:pc89282a60c09012448d6e653b68881171cd84598f9c598d0858add1c6e760224@ec2-54-78-115-33.eu-west-1.compute.amazonaws.com:6899')

TOKEN = '1462111599:AAFkLy-RZHBMW5cL01TFg0ugwtLIF-wFeSY'
bot = telebot.TeleBot(TOKEN)
value = 0
price = 0

mushroom = emojize(":mushroom:", use_aliases=True)
snowflake = emojize(":snowflake:", use_aliases=True)
lemon = emojize(":lemon:", use_aliases=True)
heart = emojize(":heart:", use_aliases=True)
rainbow = emojize(':rainbow:', use_aliases=True)
candy = emojize(":candy:", use_aliases=True)
ak = emojize(":skull:", use_aliases=True)
kokos = emojize(":coconut:", use_aliases=True)
syringe = emojize(":syringe:", use_aliases=True)


@bot.message_handler(commands=['start'])
def start_command(message):
    r.set(str(message.chat.id), str(message.from_user.username))
    r.set('messageid' + str(message.chat.id), message.message_id)
    bot.delete_message(message.chat.id, message.message_id)
    firstmenu(message)


def firstmenu(message):
    bot.clear_step_handler_by_chat_id(message.chat.id)
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Варшава', callback_data='warsaw'),
        telebot.types.InlineKeyboardButton('Лодзь', callback_data='lodz')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Познань', callback_data='poznan'),
        telebot.types.InlineKeyboardButton('Гданск', callback_data='gdansk')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Краков', callback_data='krakow'),
        telebot.types.InlineKeyboardButton('Вроцлав', callback_data='wroclaw')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Щецин', callback_data='szecyn'),
        telebot.types.InlineKeyboardButton('Быдгощ', callback_data='bydgoszcz')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Люблин', callback_data='lublin'),
        telebot.types.InlineKeyboardButton('Катовице', callback_data='katowice')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Белосток', callback_data='belostok'),
        telebot.types.InlineKeyboardButton('Гдыня', callback_data='gdynia')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Ченстхова', callback_data='czenstchowa'),
        telebot.types.InlineKeyboardButton('Радом', callback_data='radom')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отзывы', url='https://t.me/shopfenpl')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton('Написать оператору', url='t.me/narkpl')
    )
    if str(message.chat.id) == '1325770204':
        keyboard.row(
            telebot.types.InlineKeyboardButton('Отправить сообщение мамонтам', callback_data='sentmamont')
        )
    bot.send_photo(message.chat.id, 'https://telegra.ph/file/c3d1f3b30f39307418de9.png', reply_markup=keyboard)


def secondmenu(message):
    bot.delete_message(message.chat.id, message.message_id)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    if str(city) == 'Варшава':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(mushroom + 'Грибы 3г', callback_data='mushrooms1'),
            telebot.types.InlineKeyboardButton(mushroom + 'Грибы 6г', callback_data='mushrooms2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 3г', callback_data='mef3')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(kokos + 'Кокаин 1г', callback_data='cocaina')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/b07ab1d2c0e1270b7dcc1.png', reply_markup=keyboard)
    if str(city) == 'Лодзь':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/f4e6d083b4f8f2778d79d.png', reply_markup=keyboard)
    if str(city) == 'Познань':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 3г', callback_data='mef3')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/88edaf42fb8684cd7ad94.png', reply_markup=keyboard)
    if str(city) == 'Гданськ':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )
        
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/bc0479ab1f12673db7d1d.png', reply_markup=keyboard)
    if str(city) == 'Краков':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(kokos + 'Кокаин 1г', callback_data='cocaina')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/84a28a880f1640e8aacb9.png', reply_markup=keyboard)
    if str(city) == 'Вроцлав':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja LH 5г' + lemon, callback_data='weed5')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/0e535cd903de59e58228b.png', reply_markup=keyboard)
    if str(city) == 'Щецин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 2г', callback_data='weed2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/74104387863259b59aadc.png', reply_markup=keyboard)
    if str(city) == 'Быдгощ':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 2г', callback_data='weed2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja 5г', callback_data='ak3')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/c6d27af487fb5ea38da16.png', reply_markup=keyboard)
    if str(city) == 'Люблин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Кристаллы МДМА 1г', callback_data='mdma'),
            telebot.types.InlineKeyboardButton(ak + 'Гашиш Blue Berry полусинтетический 1г', callback_data='gashik')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja LH 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 1г', callback_data='alpha'),
            telebot.types.InlineKeyboardButton(snowflake + 'Кристаллы Альфы 5г', callback_data='5alpha')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/9b6c1a17a65c95ad777f6.png', reply_markup=keyboard)
    if str(city) == 'Катовице':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja LH 5г' + lemon, callback_data='weed5')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/4a9ee7974eb7f5c4720c6.png', reply_markup=keyboard)
    if str(city) == 'Белосток':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/f3d147cee9c8df6ddbe09.png', reply_markup=keyboard)
    if str(city) == 'Гдыния':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD)' + rainbow, callback_data='lsd'),
            telebot.types.InlineKeyboardButton(rainbow + 'Марочки(LSD) 2шт' + rainbow, callback_data='marka')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 1 шт', callback_data='panisher'),
            telebot.types.InlineKeyboardButton(candy + 'Таблетки Панишер 300 МДМА 5 шт', callback_data='5panisher')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/78cd9d3f252ac6773aa63.png', reply_markup=keyboard)
    if str(city) == 'Ченстхова':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 1г', callback_data='weed1'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 2г', callback_data='weed2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 5г', callback_data='ak3'),
            telebot.types.InlineKeyboardButton(lemon + 'Ganja 5г' + lemon, callback_data='weed5')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/5104964d1aba0fd6334c1.png', reply_markup=keyboard)
    if str(city) == 'Радом':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 1г', callback_data='amf1'),
            telebot.types.InlineKeyboardButton(snowflake + 'Амф HQ 2г', callback_data='amf2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 1г', callback_data='ak1'),
            telebot.types.InlineKeyboardButton(ak + 'Ganja AK47 2г', callback_data='ak2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(heart + 'Mеф 1г', callback_data='mef1'),
            telebot.types.InlineKeyboardButton(heart + 'Mеф 2г', callback_data='mef2')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton(candy + 'Экстази 1шт', callback_data='ecstasy'),
            telebot.types.InlineKeyboardButton(candy + 'Экстази 2шт', callback_data='zappa')
        )

        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu')
        )
        bot.send_photo(message.chat.id, 'https://telegra.ph/file/e25b35cc82a74e2b2906d.png', reply_markup=keyboard)


def thirdmenu(message):
    bot.delete_message(message.chat.id, message.message_id)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    if str(city) == 'Варшава':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wola', callback_data='wola'),
            telebot.types.InlineKeyboardButton('Centrum', callback_data='centrum')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Stare miasto', callback_data='oldtown'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Лодзь':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('POLESIE', callback_data='POLESIE'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('BALUTY', callback_data='BALUTY'),
            telebot.types.InlineKeyboardButton('WIDZEW', callback_data='WIDZEW')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Познань':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Nowe Miasto', callback_data='Nowe Miasto'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Zlotniki', callback_data='Zlotniki'),
            telebot.types.InlineKeyboardButton('Lubon', callback_data='Lubon')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Гданськ':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Sopot', callback_data='Sopot'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Matarnia', callback_data='Matarnia'),
            telebot.types.InlineKeyboardButton('Oliwa', callback_data='Oliwa')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Краков':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('GRZEGORZKI', callback_data='GRZEGORZKI'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Bronowice', callback_data='Bronowice'),
            telebot.types.InlineKeyboardButton('CZYZYNY', callback_data='CZYZYNY')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Вроцлав':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Poludnie', callback_data='Poludnie'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Psie Pole', callback_data='Psie Pole'),
            telebot.types.InlineKeyboardButton('Krzyki', callback_data='Krzyki')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Щецин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Warszewo', callback_data='Warszewo'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Быдгощ':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Glinki', callback_data='Glinki'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Люблин':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Wrotkow', callback_data='Wrotkow'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Rury', callback_data='Rury'),
            telebot.types.InlineKeyboardButton('Tatary', callback_data='Tatary')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Катовице':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Giszowiec', callback_data='Giszowiec'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Panewniki', callback_data='Panewniki'),
            telebot.types.InlineKeyboardButton('Chorzow', callback_data='Chorzow')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Белосток':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Sienkiewicza', callback_data='Sienkiewicza'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Гдыния':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Witomino', callback_data='Witomino'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Ченстхова':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    if str(city) == 'Радом':
        keyboard = telebot.types.InlineKeyboardMarkup()
        keyboard.row(
            telebot.types.InlineKeyboardButton('Аквапарк', callback_data='Аквапарк'),
            telebot.types.InlineKeyboardButton('ЦЕНТР', callback_data='center')
        )
        keyboard.row(
            telebot.types.InlineKeyboardButton('Назад', callback_data='backmenu'),
            telebot.types.InlineKeyboardButton('Доставка', callback_data='delivery')
        )
    bot.send_message(message.chat.id, 'Избран продукт: ' + str(staff) +
                     '\nГород: ' + str(city) +
                     '\nЦена: ' + str(price) + 'zł' +
                     '\nВыберите локацию клада или воспользуйтесь доставкой.', reply_markup=keyboard)


def rajonwars(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('ON-LINE', callback_data='online'),
        telebot.types.InlineKeyboardButton('ТЕРМИНАЛ', callback_data='terminal'),
        telebot.types.InlineKeyboardButton('Картой', callback_data='pszelew')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='backmenu')
    )
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    stuff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Заявка создана'
                                      '\nГород: ' + str(city) +
                     '\nРайон: ' + str(rajon) +
                     '\nПродукт: ' + str(stuff) +
                     '\nЦена: ' + str(price) + 'zł', reply_markup=keyboard
                     )


def online(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "zł" + "\n\n"
                                                                                  "⚠️ ВАЛЮТА BITCOIN  \n\n"
                                                                                  "👉  Для оплаты перейди по ссылке и следуй инструкциям.\n\n "
                                                                                  "🔗 https://swap.ly/ru/\n\n"
                                                                                  "⚠️ Введите сумму в соответствующем поле \n"
                                                                                  "(☑️ Для быстрого обмена рекомендуем пройти верификацию)\n\n"
                                                                                  "📨  После оплаты проверь свой E-mail и пришли боту TXid \n\n"
                                                                                  "👇 BTC АДРЕС 👇\n" + "1G4ZnnSFpYYEWppCxqB4HzM5cQkknV8Kbz",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(1325770204,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nРайон: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Online")



def terminal(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "⚠️ ВАЛЮТА BTC\n\n"
                                      "Сумма: " + str(price) + "zł" +
                     "\n\n👉 Инструкция оплаты (https://telegra.ph/OPLATA-11-11)\n\n"
                     "👇 После оплаты отправь боту точное время транзакции в формате '00:00'\n\n",
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(1325770204,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nРайон: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Terminal")



def pszelew(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('Отменить заказ', callback_data='cancleorder')
    )
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "💳 Сумма к оплате: " + str(price) + "zł" + "\n\n"
                                                                                  "⚠️ ВАЛЮТА Zlote  \n\n"
                                                                                  "👉  Для оплаты переведите " + str(
        price) + "zł моментальным платежем на наш счет.\n\n "
                 "🔗 Numer konta: 84-156-000-1320-1344-1480-000-001\n\n"
                 "📨  После оплаты пришли боту точное время транзакции \n\n", reply_markup=keyboard)
    bot.register_next_step_handler(message, obrabotka)
    city = r.get('city' + str(message.chat.id)).decode('utf-8')
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    mamont = r.get(str(message.chat.id)).decode('utf-8')
    bot.send_message(1325770204,
                     "Заявка создана\n"
                     'Город: ' + str(city) +
                     "\nРайон: " + str(rajon) +
                     "\nПродукт: " + str(staff) +
                     "\nЦена: " + str(price) +
                     "\nМамонт: @" + str(mamont) +
                     "\nID: @" + str(message.chat.id) +
                     "\nОплата: Terminal")




def obrabotka(message):
    if message.text == "back":
        bot.delete_message(message.chat.id, message.message_id - 1)
        firstmenu(message)
    else:
        bot.delete_message(message.chat.id, message.message_id)
        bot.send_message(message.chat.id, "Данные проверяются\nОжидайте ответ от оператора")
        bot.register_next_step_handler(message, obrabotka)


def delivery(message):
    bot.send_message(message.chat.id,
                     "Цена доставки: 25zł\nПосле оплаты с вами свяжется курьер\nВведите адрес доставки")
    bot.delete_message(message.chat.id, message.message_id)
    bot.register_next_step_handler(message, deliveryadress)


def deliveryadress(message):
    city = r.get("city" + str(message.chat.id)).decode('utf-8')
    r.set((str("Rajon") + str(message.chat.id)), str(message.text))
    rajon = r.get((str("Rajon") + str(message.chat.id))).decode('utf-8')
    staff = r.get((str("Staff") + str(message.chat.id))).decode('utf-8')
    price1 = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    r.set((str("Price") + str(message.chat.id)), int(price1) + 25)
    price = r.get((str("Price") + str(message.chat.id))).decode('utf-8')
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.row(
        telebot.types.InlineKeyboardButton('ON-LINE', callback_data='online'),
        telebot.types.InlineKeyboardButton('ТЕРМИНАЛ', callback_data='terminal'),
        telebot.types.InlineKeyboardButton('Картой', callback_data='pszelew')
    )
    keyboard.row(
        telebot.types.InlineKeyboardButton("Отменить заказ", callback_data='backmenu')
    )
    bot.delete_message(message.chat.id, message.message_id)
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.send_message(message.chat.id, "Ваш заказ: " + str(message.message_id) +
                     "\nГород: " + str(city) +
                     "\nАдрес доставки: " + str(rajon) +
                     "\nТовар: " + str(staff) +
                     "\nЦена: " + str(price) + "zł"
                                               "\nВыберите удобный метод оплаты: ", reply_markup=keyboard)


def sentmamont(message):
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, "Введи ID мамонта")
    bot.register_next_step_handler(message, getid)


def getid(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    bot.delete_message(message.chat.id, message.message_id)
    bot.send_message(message.chat.id, 'Что отправить ?')
    chatid = str(message.text)
    bot.register_next_step_handler(message, sendmess, chatid)


def sendmess(message, chatid):
    bot.delete_message(message.chat.id, message.message_id)
    try:
        bot.send_message(chatid, str(message.text))
    except:
        bot.send_message(message.chat.id, 'шото не так')
        firstmenu(message)
    else:
        firstmenu(message)


@bot.callback_query_handler(func=lambda call: True)
def iq_callback(query):
    data = query.data
    if data.startswith('backmenu'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        firstmenu(query.message)
    if data.startswith('warsaw'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Варшава')
        secondmenu(query.message)
    if data.startswith('lodz'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Лодзь')
        secondmenu(query.message)
    if data.startswith('poznan'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Познань')
        secondmenu(query.message)
    if data.startswith('gdansk'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Гданськ')
        secondmenu(query.message)
    if data.startswith('krakow'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Краков')
        secondmenu(query.message)
    if data.startswith('wroclaw'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Вроцлав')
        secondmenu(query.message)
    if data.startswith('szecyn'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Щецин')
        secondmenu(query.message)
    if data.startswith('bydgoszcz'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Быдгощ')
        secondmenu(query.message)
    if data.startswith('lublin'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Люблин')
        secondmenu(query.message)
    if data.startswith('katowice'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Катовице')
        secondmenu(query.message)
    if data.startswith('belostok'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Белосток')
        secondmenu(query.message)
    if data.startswith('gdynia'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Гдыния')
        secondmenu(query.message)
    if data.startswith('czenstchowa'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Ченстхова')
        secondmenu(query.message)
    if data.startswith('radom'):
        bot.answer_callback_query(query.id)
        r.set('city' + str(query.message.chat.id), 'Радом')
        secondmenu(query.message)
    if data.startswith('amf1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на амф")
        \
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 1г")
        r.set((str("Price") + str(query.message.chat.id)), "50")
        thirdmenu(query.message)
    if data.startswith('amf2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на амф")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Амф 2г")
        r.set((str("Price") + str(query.message.chat.id)), "80")
        thirdmenu(query.message)
    if data.startswith('weed1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Ganja 1г")
        r.set((str("Price") + str(query.message.chat.id)), "50")
        thirdmenu(query.message)
    if data.startswith('weed2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Ganja 2г")
        r.set((str("Price") + str(query.message.chat.id)), "100")
        thirdmenu(query.message)
    if data.startswith('weed5'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Ganja 5г")
        r.set((str("Price") + str(query.message.chat.id)), "200")
        thirdmenu(query.message)
    if data.startswith('ak1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Ganja AK47 1г")
        r.set((str("Price") + str(query.message.chat.id)), "60")
        thirdmenu(query.message)
    if data.startswith('ak2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Ganja AK47 2г")
        r.set((str("Price") + str(query.message.chat.id)), "120")
        thirdmenu(query.message)
    if data.startswith('ak3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на шмаль")
        
        r.set((str("Staff") + str(query.message.chat.id)), "GanjaGanja AK47 5г")
        r.set((str("Price") + str(query.message.chat.id)), "250")
        thirdmenu(query.message)
    if data.startswith('mef1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 1г")
        r.set((str("Price") + str(query.message.chat.id)), "80")
        thirdmenu(query.message)
    if data.startswith('mef2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 2г")
        r.set((str("Price") + str(query.message.chat.id)), "150")
        thirdmenu(query.message)
    if data.startswith('mef3'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на мефедрон")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Мефедрон 3г")
        r.set((str("Price") + str(query.message.chat.id)), "220")
        thirdmenu(query.message)
    if data.startswith('mushrooms1'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 3г")
        r.set((str("Price") + str(query.message.chat.id)), "100")
        thirdmenu(query.message)
    if data.startswith('mushrooms2'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на грибы")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Грибы 6г")
        r.set((str("Price") + str(query.message.chat.id)), "200")
        thirdmenu(query.message)
    if data.startswith('lsd'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на марки")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD)")
        r.set((str("Price") + str(query.message.chat.id)), "60")
        thirdmenu(query.message)
    if data.startswith('marka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на марки")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Марка(LSD) 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "120")
        thirdmenu(query.message)
    if data.startswith('ecstasy'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "50")
        thirdmenu(query.message)
    if data.startswith('lalka'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 5шт")
        r.set((str("Price") + str(query.message.chat.id)), "220")
        thirdmenu(query.message)
    if data.startswith('zappa'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на таблетки")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Экстази 2шт")
        r.set((str("Price") + str(query.message.chat.id)), "100")
        thirdmenu(query.message)
    if data.startswith('cocaina'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на кокс")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Кокаин 1г")
        r.set((str("Price") + str(query.message.chat.id)), "450")
        thirdmenu(query.message)
    if data.startswith('subitex'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на субитекс")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Субитекс 1шт")
        r.set((str("Price") + str(query.message.chat.id)), "50")
        thirdmenu(query.message)


    if data.startswith('gashik'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на Гашиш")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Гашиш Blue Berry полусинтетический 1 г")
        r.set((str("Price") + str(query.message.chat.id)), "120")
        thirdmenu(query.message)
    if data.startswith('mdma'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на Кристаллы")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Кристаллы МДМА 1 г")
        r.set((str("Price") + str(query.message.chat.id)), "150")
        thirdmenu(query.message)
    if data.startswith('alpha'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на Альфy")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Кристаллы Альфы 1 г")
        r.set((str("Price") + str(query.message.chat.id)), "80")
        thirdmenu(query.message)
    if data.startswith('5alpha'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на Кристаллы")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Кристаллы Альфы 5 г")
        r.set((str("Price") + str(query.message.chat.id)), "300")
        thirdmenu(query.message)
    if data.startswith('panisher'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на Панишер")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Панишер 300 МДМА 1 шт")
        r.set((str("Price") + str(query.message.chat.id)), "85")
        thirdmenu(query.message)
    if data.startswith('5panisher'):
        bot.answer_callback_query(query.id)
        user = r.get(query.message.chat.id).decode('utf-8')
        city = r.get('city' + str(query.message.chat.id)).decode('utf-8')
        bot.send_message(1325770204, "@" + str(user) + " из города " + str(city) + " втыкает на Панишер")
        
        r.set((str("Staff") + str(query.message.chat.id)), "Таблетки Панишер 300 МДМА 5 шт")
        r.set((str("Price") + str(query.message.chat.id)), "350")
        thirdmenu(query.message)


    if data.startswith('wola'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Воля")
        rajonwars(query.message)
    if data.startswith('centrum'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Центрум")
        rajonwars(query.message)
    if data.startswith('oldtown'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Stare miasto")
        rajonwars(query.message)
    if data.startswith('delivery'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "delivery")
        delivery(query.message)
    if data.startswith('POLESIE'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "POLESIE")
        rajonwars(query.message)
    if data.startswith('center'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Центр")
        rajonwars(query.message)
    if data.startswith('GRZEGORZKI'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "GRZEGORZKI")
        rajonwars(query.message)
    if data.startswith('Nowe Miasto'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Nowe Miasto")
        rajonwars(query.message)
    if data.startswith('Poludnie'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Poludnie")
        rajonwars(query.message)
    if data.startswith('Warszewo'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Warszewo")
        rajonwars(query.message)
    if data.startswith('Glinki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Glinki")
        rajonwars(query.message)
    if data.startswith('Wrotkow'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Wrotkow")
        rajonwars(query.message)
    if data.startswith('Giszowiec'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Giszowiec")
        rajonwars(query.message)
    if data.startswith('Sienkiewicza'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Sienkiewicza")
        rajonwars(query.message)
    if data.startswith('Witomino'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Witomino")
        rajonwars(query.message)
    if data.startswith('Аквапарк'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Аквапарк")
        rajonwars(query.message)
    if data.startswith('BALUTY'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "BALUTY")
        rajonwars(query.message)
    if data.startswith('WIDZEW'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "WIDZEW")
        rajonwars(query.message)
    if data.startswith('Zlotniki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Zlotniki")
        rajonwars(query.message)
    if data.startswith('Lubon'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Lubon")
        rajonwars(query.message)
    if data.startswith('Matarnia'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Matarnia")
        rajonwars(query.message)
    if data.startswith('Oliwa'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Oliwa")
        rajonwars(query.message)
    if data.startswith('Bronowice'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Bronowice")
        rajonwars(query.message)
    if data.startswith('CZYZYNY'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "CZYZYNY")
        rajonwars(query.message)
    if data.startswith('Psie Pole'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Psie Pole")
        rajonwars(query.message)
    if data.startswith('Krzyki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Krzyki")
        rajonwars(query.message)
    if data.startswith('Rury'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Rury")
        rajonwars(query.message)
    if data.startswith('Tatary'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Tatary")
        rajonwars(query.message)
    if data.startswith('Panewniki'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Panewniki")
        rajonwars(query.message)
    if data.startswith('Chorzow'):
        bot.answer_callback_query(query.id)
        r.set((str("Rajon") + str(query.message.chat.id)), "Chorzow")
        rajonwars(query.message)
    if data.startswith('cancleorder'):
        bot.answer_callback_query(query.id)
        bot.delete_message(query.message.chat.id, query.message.message_id)
        firstmenu(query.message)
    if data.startswith('online'):
        bot.answer_callback_query(query.id)
        online(query.message)
    if data.startswith('terminal'):
        bot.answer_callback_query(query.id)
        terminal(query.message)
    if data.startswith('pszelew'):
        bot.answer_callback_query(query.id)
        pszelew(query.message)
    if data.startswith('sentmamont'):
        bot.answer_callback_query(query.id)
        sentmamont(query.message)


bot.polling(none_stop=True)
