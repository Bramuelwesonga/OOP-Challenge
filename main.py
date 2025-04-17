from pet import Pet

# Ask the user to name their pet
pet_name = input("🐶 What would you like to name your pet? ")
my_pet = Pet(pet_name)

# Interactive menu
def show_menu():
    print("\nWhat would you like to do?")
    print("1. Feed your pet")
    print("2. Let your pet sleep")
    print("3. Play with your pet")
    print("4. Train your pet")
    print("5. Show learned tricks")
    print("6. Check status")
    print("7. Exit")

while True:
    show_menu()
    choice = input("👉 Enter your choice (1–7): ")

    if choice == "1":
        my_pet.eat()
    elif choice == "2":
        my_pet.sleep()
    elif choice == "3":
        my_pet.play()
    elif choice == "4":
        trick = input("🧠 Enter the trick you want to teach: ")
        my_pet.train(trick)
    elif choice == "5":
        my_pet.show_tricks()
    elif choice == "6":
        my_pet.get_status()
    elif choice == "7":
        print(f"👋 Goodbye! {my_pet.name} will miss you!")
        break
    else:
        print("❌ Invalid choice. Please pick a number from 1 to 7.")
