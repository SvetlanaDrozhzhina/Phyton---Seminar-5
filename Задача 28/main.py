def sum(a, b):
  if b == 0:
    return a
  else:
    return sum(a+1, b-1)
a = int(input("Введите первое число a: "))
b = int(input("Введите второе число b: "))
print(f"Сумма чисел {a} и {b} равна {sum(a, b)}")