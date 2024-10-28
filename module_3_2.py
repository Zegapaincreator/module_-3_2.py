def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    recipient_ending = False
    sender_ending = False
    endings = ['.com', '.net', '.ru']
    recipient_ending = any(recipient.endswith(i) for i in endings)
    sender_ending = any(sender.endswith(i) for i in endings)

    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif '@' in recipient and '@' in sender and recipient_ending and sender_ending:
        if sender == 'university.help@gmail.com':
            print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>')
        else:
            print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.')
    else:
        print(f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>"')

send_email('Hello', 'pochta.ru', sender='goohagis2@l.ru')