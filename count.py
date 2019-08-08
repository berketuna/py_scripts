def count(sequence,item):
  counter = 0
  for number in sequence:
    if number == item:
      counter += 1
  return counter
