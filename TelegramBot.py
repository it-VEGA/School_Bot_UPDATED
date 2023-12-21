import telebot
import sqlite3
from telebot import types
import time
import MiddleWare as MW
import Classes as target
bot = telebot.TeleBot('5781161941:AAHfOSw8RxRzZ6k02BN7h9euS9qIclb_F0A')

def show_current_class(class_value,chat_id):
    connection = sqlite3.connect("Database.db")
    cur = connection.cursor()
    sql = "SELECT ID,FIO FROM data WHERE Class = ?"
    for item in cur.execute(sql, (class_value,)):
           bot.send_message(chat_id,text=f"{item[0]}.{item[1]}\n")
def add_current_student(user_message,chat_id):
    student_id = MW.formating_string(user_message)
    connection = sqlite3.connect("Database.db")
    cur = connection.cursor()
    sql = "SELECT Class,FIO,Adres FROM data WHERE ID = ?"
    for item in cur.execute(sql, (student_id[0],)):
           target = f"{item[0]}--{item[1]}--{item[2]}--{student_id[1]}"
           get_data_for_excel = target.split("--")
           MW.add_to_excel(get_data_for_excel)
           bot.send_message(chat_id,text=f"Ученик {get_data_for_excel[1]} отмечен как отсутствующий!")
def btn_for_2_class(first_class_vlaue,second_class_value,chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(first_class_vlaue)
    btn2 = types.KeyboardButton(second_class_value)
    markup.add(btn1, btn2)
    bot.send_message(chat_id, "Выберите класс:", reply_markup=markup)
    #
def btn_for_3_class(first_class_vlaue,second_class_value,third_class_value,chat_id):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(first_class_vlaue)
    btn2 = types.KeyboardButton(second_class_value)
    btn3 = types.KeyboardButton(third_class_value)
    markup.add(btn1, btn2, btn3)
    bot.send_message(chat_id, "Выберите класс:", reply_markup=markup)
    #
def show_and_add_2_class(msg_text,chat_id,class_value,second_class_value):
    if msg_text == class_value:
        show_current_class(class_value,chat_id)
    elif msg_text == second_class_value:
        show_current_class(second_class_value,chat_id)
    else:
        add_current_student(msg_text,chat_id)
def show_and_add_3_class(msg_text,chat_id,class_value,second_class_value,third_class_value):
    if msg_text == class_value:
        show_current_class(class_value,chat_id)
    elif msg_text == second_class_value:
        show_current_class(second_class_value,chat_id)
    elif msg_text == third_class_value:
        show_current_class(third_class_value,chat_id)
    else:
        add_current_student(msg_text,chat_id)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id,text = 'Выберите номер ученика, а затем напишите причину отсутствия\nНапример:\n\n23 Болеет (Нажимаем отправить)\n12 Грипп (Нажимаем отправить)\n29 сем.обст (Нажимаем отправить)\n')

@bot.message_handler(commands = ['start'])
def check_user(message):
    if message.from_user.id == '1420341386':
        bot.send_message(message.chat.id,text=f"Добро пожаловать - {message.from_user.first_name}")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Проверить")
        btn2 = types.KeyboardButton('Скачать отчет')
        markup.add(btn1, btn2)
        bot.send_message(message.from_user.id, "Что нужно сделать?", reply_markup=markup)
    # ОДИН КЛАСС
    elif message.from_user.id in target.single_Class.keys():
        bot.send_message(message.chat.id,text=f"Приветстую кл.рук - {message.from_user.first_name}\nСекунду показываю ваш класс...")
        time.sleep(3)
        show_current_class(target.single_Class.get(message.from_user.id),message.chat.id)
    # КОНЕЦ ОДИН КЛАСС
    # ДВА КЛАССА
    elif message.from_user.id == 527975492:
        btn_for_2_class("2А","4А",message.chat.id)
    elif message.from_user.id == 52506599:
        btn_for_2_class("10Ж","10З",message.chat.id)
    elif message.from_user.id == 377026926:
        btn_for_2_class("3Б","4Е",message.chat.id)
    elif message.from_user.id == 191395175:
        btn_for_2_class("5Г","8Г",message.chat.id)
    elif message.from_user.id == 287178175:
        btn_for_2_class("6В","9Г",message.chat.id)
    elif message.from_user.id == 762374884:
        btn_for_2_class("8З","8К",message.chat.id)
    elif message.from_user.id == 318588901:
        btn_for_2_class("1В","2В",message.chat.id)
    elif message.from_user.id == 885623096:
        btn_for_2_class("1Д","4Ж",message.chat.id)
    elif message.from_user.id == 6674731592:
        btn_for_2_class("7В","10Г",message.chat.id)
    elif message.from_user.id == 144445349:
        btn_for_2_class("2Б","4Б",message.chat.id)
    elif message.from_user.id == 322543877:
        btn_for_2_class("8И","10В",message.chat.id)
    elif message.from_user.id == 519479493:
        btn_for_2_class("5В","9В",message.chat.id)
    elif message.from_user.id == 213694423:
        btn_for_2_class("1Б","4В",message.chat.id)
    elif message.from_user.id == 547077959:
        btn_for_2_class("1Е","2Г",message.chat.id)
    elif message.from_user.id == 505043325:
        btn_for_2_class("1З","4Д",message.chat.id)
    elif message.from_user.id == 743816897:
        btn_for_2_class("1Г","4Г",message.chat.id)
    elif message.from_user.id == 715911475:
        btn_for_2_class("3А","4З",message.chat.id)
    elif message.from_user.id == 525507572:
        btn_for_2_class("1Ж","3Е",message.chat.id)
    elif message.from_user.id == 890159680:
        btn_for_2_class("8А","9Е",message.chat.id)
    elif message.from_user.id == 6674731592:
        btn_for_2_class("7В","10Г",message.chat.id)
    elif message.from_user.id == 434299119:
        btn_for_2_class("1А","3Г",message.chat.id)
    elif message.from_user.id == 234881707:
        btn_for_2_class("8Е","9К",message.chat.id)
    # ТРИ КЛАССА
    elif message.from_user.id == 2071879094:
        btn_for_3_class("8Л","8Д","5Д",message.chat.id)
    elif message.from_user.id == 450047259:
        btn_for_3_class("8В","9Ж","11З",message.chat.id)
    elif message.from_user.id == 615991166:
        btn_for_3_class("5Б","9Д","11А",message.chat.id)
    #
    else:
        bot.send_message(message.chat.id,text="Доступ запрещен")
# ....................................................  #
@bot.message_handler(content_types=['text'])
def get_text_msg(message):
    # ОДИН КЛАСС
    single_Class = [1845649095,5680312753,257735249,1436773655,617085152,482826888,1816497015,264580093,167061243,167061243,390196081,326584999,300110939,851573556,605124630,39733898,694868265]
    if message.from_user.id in single_Class:
        add_current_student(message.text,message.chat.id)
    # КОНЕЦ ОДИН КЛАСС
    # ДВА КЛАССА         
    elif message.from_user.id == 527975492:
        show_and_add_2_class(message.text,message.chat.id,"2А","4А")
    elif message.from_user.id == 52506599:
        show_and_add_2_class(message.text,message.chat.id,"10Ж","10З")
    elif message.from_user.id == 377026926:
        show_and_add_2_class(message.text,message.chat.id,"3Б","4Е")
    elif message.from_user.id == 191395175:
        show_and_add_2_class(message.text,message.chat.id,"5Г","8Г")
    elif message.from_user.id == 287178175:
        show_and_add_2_class(message.text,message.chat.id,"6В","9Г")
    elif message.from_user.id == 762374884:
        show_and_add_2_class(message.text,message.chat.id,"8З","8К")
    elif message.from_user.id == 318588901:
        show_and_add_2_class(message.text,message.chat.id,"1В","2В")
    elif message.from_user.id == 885623096:
        show_and_add_2_class(message.text,message.chat.id,"1Д","4Ж")
    elif message.from_user.id == 6674731592:
        show_and_add_2_class(message.text,message.chat.id,"7В","10Г")
    elif message.from_user.id == 144445349:
        show_and_add_2_class(message.text,message.chat.id,"2Б","4Б")
    elif message.from_user.id == 322543877:
        show_and_add_2_class(message.text,message.chat.id,"8И","10В")
    elif message.from_user.id == 519479493:
        show_and_add_2_class(message.text,message.chat.id,"5В","9В")
    elif message.from_user.id == 213694423:
        show_and_add_2_class(message.text,message.chat.id,"1Б","4В")
    elif message.from_user.id == 547077959:
        show_and_add_2_class(message.text,message.chat.id,"1Е","2Г")
    elif message.from_user.id == 505043325:
        show_and_add_2_class(message.text,message.chat.id,"1З","4Д")
    elif message.from_user.id == 743816897:
        show_and_add_2_class(message.text,message.chat.id,"1Г","4Г")
    elif message.from_user.id == 715911475:
        show_and_add_2_class(message.text,message.chat.id,"3А","4З")
    elif message.from_user.id == 525507572:
        show_and_add_2_class(message.text,message.chat.id,"1Ж","3Е")
    elif message.from_user.id == 890159680:
        show_and_add_2_class(message.text,message.chat.id,"8А","9Е")
    elif message.from_user.id == 6674731592:
        show_and_add_2_class(message.text,message.chat.id,"7В","10Г")
    elif message.from_user.id == 434299119:
        show_and_add_2_class(message.text,message.chat.id,"1А","3Г")
    elif message.from_user.id == 234881707:
        show_and_add_2_class(message.text,message.chat.id,"8Е","9К")
    #
    # ТРИ КЛАССА
    elif message.from_user.id == 2071879094:
        show_and_add_3_class(message.text,message.chat.id,"8Л","8Д","5Д")
    elif message.from_user.id == 450047259:
        show_and_add_3_class(message.text,message.chat.id,"8В","9Ж","11З")
    elif message.from_user.id == 615991166:
        show_and_add_3_class(message.text,message.chat.id,"5Б","9Д","11А")
    #
    else:
        bot.send_message(message.chat.id,text=f"Что-то пошло не так!Не смог отметить ученика.{message.text}")
if __name__ == "__main__":
    print("******************************\n******* СЕРВЕР ЗАПУЩЕН *******\n******************************")
    bot.polling(none_stop=True, interval=0)