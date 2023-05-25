# Функция возврата списка четных чисел из списка
def get_even(lst):
  result = list(filter(lambda x: x % 2 == 0, lst))
  return result
