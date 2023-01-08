import telebot
import sqlite3 as sq

bot = telebot.TeleBot('5958548074:AAHGN8-XDcYDN5KFqm6seTYtC7kozOFj6c4')


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Hello world')


@bot.message_handler(commands=['start'])
def start(message):
    connect = sq.connect('users.db')
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS test1(
        id INTEGER
    )""")

    connect.commit()


    people_id = message.chat.id
    cursor.execute(f"SELECT id FROM test1 WHERE id = {people_id}")
    data = cursor.fetchone()
    if data is None:
        user_id = [(message.chat.id)]
        cursor.execute("INSERT INTO test1 VALUES (?);", user_id)
        bot.send_message(message.chat.id, 'Your id has been registered')
        connect.commit()
    else:
        bot.send_message(message.chat.id, 'Your id Already exists')

@bot.message_handler(commands=['delete'])
def delete(message):
    connect = sq.connect('users.db')
    cursor = connect.cursor()

    people_id = message.chat.id
    cursor.execute(f"DELETE FROM test1 WHERE id = {people_id}")
    bot.send_message(message.chat.id, 'Your id has been deleted')
    connect.commit()

bot.polling(none_stop=True)
