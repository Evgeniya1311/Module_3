def send_email(message, recipient, sender = "university.help@gmail.com"):
    #Проверка корректности введеных email-адресов
    if recipient.rfind('@') == -1 or sender.rfind('@') == -1:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient.rfind('.com') == -1 and recipient.rfind('.ru') == -1 and recipient.rfind('.net') == -1:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif sender.rfind('.com') == -1 and sender.rfind('.ru') == -1 and sender.rfind('.net') == -1:
        return print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}')
    elif recipient == sender:
        return print("Невозможно отправить письмо самому себе")
    #Проверка отправителя
    if sender == "university.help@gmail.com":
        return print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        return print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


#send_email('Hi', 'zhe50404156@gmail.com')
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
