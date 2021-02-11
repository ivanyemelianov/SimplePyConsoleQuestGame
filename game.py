print("Welcome to your first game!")
name = input("What is your name? ")
age = int(input("Wha is your age? "))

print("Hello", name, "you are", age, "years old.")

health = 10

print("You start with", health, "health.")

if age >= 18:
    print("You're old enough")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Lets play!")

        left_or_right = input("First choice... Left or Right? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path and reach a lake... Do you swim across or go around? ")

            if ans == "around":
                print("You went around and reached the other side of the lake.")
            elif ans == "across":
                print("You were able to get across but were bit by a fish and lost 5 health.")
                health -= 5

            ans = input("You notice a house and a river. Which do you go to (river/house)? ")

            if ans == "house":
                print("You go to the hosue and greeted by the owner... He doesn't like and you lose 5 health.")
                health -= 5

                if health <= 0:
                    print("You have 0 health and you died...")
                else:
                    print("You survived!!!")

            else:
                print("You died in the river.")           
        else:
            print("You fell down and lost...")
    else:
        print("Cya...")
else:
    print("You're not old enough to play")
