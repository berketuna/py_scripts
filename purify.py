def purify(numbers):
  even_list = []
  for number in numbers:
    reminder = number % 2
    if reminder == 0:
      even_list.append(number)
  return even_list
