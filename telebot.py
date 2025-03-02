import telebot
import datetime
import time
import threading
import random

bot = telebot.TeleBot("8179239880:AAEKjyy0CfWg81yx8FPvUu27NoF_uhbxiWY")

list = ["**Вода на Земле может быть старше самой Солнечной системы**: Исследования показывают, что от 30% до 50% воды в наших океанах возможно присутствовала в межзвездном пространстве еще до формирования Солнечной системы около 4,6 миллиарда лет назад.",
"**Горячая вода замерзает быстрее холодной**: Это явление известно как эффект Мпемба. Под определенными условиями горячая вода может замерзать быстрее, чем холодная, хотя ученые до сих пор полностью не разгадали механизм этого процесса.",
"**Больше воды в атмосфере, чем во всех реках мира**: Объем водяного пара в атмосфере Земли в любой момент времени превышает объем воды во всех реках мира вместе взятых. Это подчеркивает важную роль атмосферы в гидрологическом цикле, перераспределяя воду по планете."]

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить воду и кофе!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,))
    reminder_thread.start()

@bot.message_handler(commands=['fact'])
def fact_message(message):
    random_fact = random.choice(list)
    bot.reply_to(message, f'Лови факт о воде {random_fact}')

# Новая команда для расчета дневной нормы воды
@bot.message_handler(commands=['calculate'])
def calculate_daily_water_norm(message):
    bot.send_message(message.chat.id, 'Пожалуйста, введите Ваш вес в килограммах.')
    bot.register_next_step_handler(message, process_weight_input)

def process_weight_input(message):
    try:
        weight = float(message.text)  # Преобразовываем ввод в число
        daily_water_norm = weight * 0.033  # Расчёт дневной нормы воды
        daily_water_norm = round(daily_water_norm, 2)  # Округляем до двух знаков после запятой
        bot.send_message(
            message.chat.id,
            f"Ваша суточная норма воды составляет примерно {daily_water_norm} литров."
        )
    except ValueError:
        bot.send_message(message.chat.id, 'Не удалось распознать вес. Пожалуйста, попробуйте снова.')

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def help_command(message):
    help_text = """*Доступные команды:* /start — начальная настройка бота /calculate — расчет суточной нормы воды /fact — интересный факт о воде /help — справка по доступным командам *Как работает бот:* Бот регулярно напоминает вам пить воду и помогает рассчитать вашу суточную норму воды."""
    bot.send_message(message.chat.id, help_text, parse_mode='MarkdownV2')  # Форматируем текст с помощью MarkdownV2

def send_reminders(chat_id):
    first_rem = "12:42"
    second_rem = "14:00"
    end_rem = "18:00"


    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == first_rem or now == second_rem or now == end_rem:
            bot.send_message(chat_id, "Напоминание - выпей стакан воды")
            time.sleep(61)
        time.sleep(1)

bot.polling(none_stop=True)