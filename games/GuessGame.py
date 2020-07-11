import random
import time
holy_grail = random.randint(1, 100)
trials = []
print("Hey, pilgrim!")
print("""You should guess a number within 1 and 100 borders. 
        \nOn you very first try: If you're not as far from the goal as 10 points - 
        the Dragon's nest will shout at you: 'WARM!'
        \nand 'COLD!'' otherwise. 
        \nIt should be a piece of cake for you - cause it will help you even further - shouting 'WARMER!'
        \nif any of your subsequent quesses are closer to goal then previous but 'COLDER!' otherwise""")
time.sleep(2)

while True:
    try:
        guess = int(input("Your guess?\n"))
    except ValueError:
        continue
    trials.append(guess)
    trials_amount = len(trials)
    if guess == holy_grail:
        print(f"Congrats lucky! It took only {trials_amount} tries.")
        break

    diff = abs(holy_grail - guess)
    if trials_amount > 1:
        if diff < abs(holy_grail - trials[-2]):
            print("WARMER!")
        else:
            print("COLDER!")
    else:
        if diff <= 10:
            print("WARM!")
        else:
            print("COLD!")