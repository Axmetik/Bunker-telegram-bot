#імпорт модулів та файлів
import telebot
from telebot import types
import bunker
import person
import story
import messages
import adding


#пдіключення бота через унікальний токен
bot = telebot.TeleBot(***) //unique token

#Хендлер для прийому команди /start
@bot.message_handler(commands=['start'])
def start(mess):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    story_btn = types.KeyboardButton('📚Історія')
    person_btn = types.KeyboardButton('👨Персона👩')
    bunker_btn = types.KeyboardButton('☠Бункер')
    rules_btn = types.KeyboardButton('📝Правила')
    add_btn = types.KeyboardButton('✏Відгуки')

    markup.add(person_btn, bunker_btn, story_btn, rules_btn, add_btn)

    bot.send_message(mess.chat.id, messages.start)
    bot.send_message(mess.chat.id, 'Оберіть дію', reply_markup=markup)


#Хендлер для прийому тексту(кнопки)
@bot.message_handler(content_types=['text'])
def buttons(message):
    if message.text == '📚Історія':
        st = story.story()
        bot.send_message(message.chat.id, st.getStory())

    elif message.text == '👨Персона👩':
        prs = person.person()
        prs.setPerson()
        bot.send_message(message.chat.id, prs.getPerson())

    elif message.text == '📝Правила':
        bot.send_message(message.chat.id, messages.rules)

    elif message.text == '☠Бункер':
        bn = bunker.bunker()
        bn.setBunker()
        bot.send_message(message.chat.id, bn.getBunker())

    elif message.text == '🔙Назад':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        story_btn = types.KeyboardButton('📚Історія')
        person_btn = types.KeyboardButton('👨Персона👩')
        bunker_btn = types.KeyboardButton('☠Бункер')
        rules_btn = types.KeyboardButton('📝Правила')
        add_btn = types.KeyboardButton('✏Відгуки')

        markup.add(person_btn, bunker_btn, story_btn, rules_btn, add_btn)

        bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)

    elif message.text == '✏Відгуки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        back_btn = types.KeyboardButton('🔙Назад')
        markup.add(back_btn)
        add_prop = bot.send_message(message.chat.id, messages.proposition, reply_markup=markup)
        bot.register_next_step_handler(add_prop, prop)


def prop(message):
    if message.text != '🔙Назад':
        adding.addProp(message.text)
        bot.send_message(message.chat.id, messages.thank)
        bot.send_message(chat_id='-898448137', text=message.text)

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        story_btn = types.KeyboardButton('📚Історія')
        person_btn = types.KeyboardButton('👨Персона👩')
        bunker_btn = types.KeyboardButton('☠Бункер')
        rules_btn = types.KeyboardButton('📝Правила')
        add_btn = types.KeyboardButton('✏Відгуки')

        markup.add(person_btn, bunker_btn, story_btn, rules_btn, add_btn)

        bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        story_btn = types.KeyboardButton('📚Історія')
        person_btn = types.KeyboardButton('👨Персона👩')
        bunker_btn = types.KeyboardButton('☠Бункер')
        rules_btn = types.KeyboardButton('📝Правила')
        add_btn = types.KeyboardButton('✏Відгуки')

        markup.add(person_btn, bunker_btn, story_btn, rules_btn, add_btn)

        bot.send_message(message.chat.id, 'Оберіть дію', reply_markup=markup)


bot.polling(none_stop=True)
