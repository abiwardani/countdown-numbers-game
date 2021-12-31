import countdown_game as cg

target_num = 312
numbers = [10, 12, 3, 62, 7, 6]

countdown = cg.Countdown(target_num, numbers)
result = countdown.search()

print(result)