# Geoffrey Tang
first = True
while True:
    if first:
        reset = False
        print("------------------------------------------------------------")
        print("Type \"reset\" at any point to restart.")
        # input range
        start = str(input("Enter minimum number: "))
        if start.lower() == "reset":
            continue
        else:
            start = int(start)
        incorrect = True
        while incorrect and not reset:
            # forces user to pick a maximum bigger than the minimum
            print("------------------------------------------------------------")
            end = str(input("Enter maximum number: "))
            if end.lower() == "reset":
                reset = True
                break
            elif int(end) > start:
                incorrect = False
                end = int(end)
        incorrect = True
        while incorrect and not reset:
            # forces user to pick a number within the specified range
            print("------------------------------------------------------------")
            chosen = str(input("Pick a number within the specified range: "))
            if chosen.lower() == "reset":
                reset = True
                break
            elif start <= int(chosen) <= end:
                incorrect = False
                chosen = int(chosen)
        if reset:
            continue
        # marks the start and end of the list to be considered and the number to be guessed
        # e.g. if left = 1, right = 5, and middle = 3, then the list to be considered is everything from index 1
        # to index 5, and the computer will guess 3
        left = start
        right = end
        middle = (left + right)//2
        score = 0
        first = False
        used = []
    print("------------------------------------------------------------")
    if middle in used:
        middle += 1
    print(middle)
    score += 1
    if middle == chosen:
        # when correct number is chosen, automatically tell user number of guesses and ask to play again
        print("------------------------------------------------------------")
        if score == 1:
            print("Your number was guessed in 1 guess.")
        else:
            print("Your number was guessed in " + str(score) + " guesses.")
        again = input("Again? (Y/N) ")
        if again.lower() == "n" or again.lower() == "no":
            break
        else:
            first = True
    else:
        used.append(middle)
        comparison = input("Too high or too low? (H/L) (Your original number: " + str(chosen) + ") ")
        incorrect = True
        while incorrect:
            if comparison.lower() == "l" or comparison.lower() == "low":
                # if guess is too low, then we know that everything lower than the guess is also too low and we don't need
                # to consider it, so we move the lower end of the range to where the guess was and set the guess to the
                # number in the middle of the start and end of the range
                left = middle
                middle = (right + left)//2
                incorrect = False
            elif comparison.lower() == "h" or comparison.lower() == "high":
                # if guess is too high, then we know that everything higher than the guess is also too high and we don't
                # need to consider it, so we move the upper end of the range to where the guess was and set the guess to the
                # number in the middle of the start and end of the range
                right = middle
                middle = (right + left)//2
                incorrect = False
            elif comparison.lower() == "reset":
                reset = True
                incorrect = False
        if reset:
            first = True
            continue
