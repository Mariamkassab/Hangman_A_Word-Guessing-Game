def check():
    global trials
    let = input("let's try a character from the word:  ")

    if let in guessed_chars:
        print("You already guessed that character. Try again.")
        check()

    if let in randomitem:
        global right
        right +=1
        if right == len(randomitem):
            print("congratulations, you did it...!  :) ")
            exit()
        else:
            print("perfect, guess another character..! ")
            guessed_chars.add(let)
            # if the word have more than 1 character are the same, there will be a bug
            check()
    else:
        trials -= 1

    if trials == 0:
        print("GAME OVER....!")
        exit()
    else:
        print("Try Again")
        check()

