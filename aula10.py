from datetime import date, time, datetime, timedelta


def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual.strftime('%c'))
    tupla = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2021, 10, 28, 18, 30)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_str = '01/01/2019 12:20:22'
    data_convertida = datetime.strptime(data_str, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data = data_convertida - timedelta(days=365, hours=2, minutes=15)
    print(nova_data)


def trabalhando_com_date():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A, %B(%Y)')
    print(data_atual_str)


def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario)


if __name__ == '__main__':
    # trabalhando_com_date()
    # trabalhando_com_time()
    trabalhando_com_datetime()
