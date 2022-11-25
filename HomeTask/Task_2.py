"""Пользователь вводит время в секундах. Переведите время в часы, минуты и
секунды и выведите в формате чч:мм:сс. Используйте форматирование строк. """
user_time = int(input('Введите время  :'))
ours = user_time // 3600
minutes = (user_time - ours*3600) // 60
seconds = user_time - ours * 3600 - minutes * 60
print(f"чч:мм:сс  {ours}:{minutes}:{seconds}")
