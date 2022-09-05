def the_perfect_guessing_game():
    import random
    comp=random.randint(1,100)
    user=None
    count=0
    while (user!=comp):
        user=int(input("Enter a value what can be a perfect guess\n"))
        count+=1
        if (user==comp):
            print("Congrats! You guess it right")
        else:
            if (user>comp):
                print("You are too far from the perfect Number, Enter a bit Smaller Number")
            elif (user<comp):
                print("You are not too far from the perfect Number, Enter a bit larger number")
    print(f"You guess the correct Number in {count} guesses")
the_perfect_guessing_game()