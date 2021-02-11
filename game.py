print("Welcome to your first game!")
name = input("What is your name? ")
age = int(input("Wha is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10

print("You start with " + health + "health.")

if age >= 18:
    print("You're old enough")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Lets play!")

        left_or_right = input("First choice... Left or Right? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around? ")

            if ans == "across":

            else:
                print("You lost.")
        else:
            print("You fell down and lost...")
    else:
        print("Cya...")

else:
    print("You're not old enough to play")
