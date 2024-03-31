import random

def print_header():
    print("")
    print("Muhammad Rifky Athaya(21120123140129)")
    print("Alfarel Nawall Putra Shadat (21120123140140)")
    print("Muhammad Romeo Raffael (21120123140151)")
    print("Rabelva Evan Ligar (21120123140161)")
    print("")
    print("")
    print("=============================================")
    print("game batu gunting kertas sederhana".center(40))
    print("==============================================")
    print("")
    print("")

def get_user_choice():
    return input("Masukkan nama Anda: ")

def get_computer_choice():
    return str(random.randint(1, 3))

def determine_winner(user_choice, computer_choice, user_name):
    if user_choice == computer_choice:
        return "Seri"
    elif (
        (user_choice == "1" and computer_choice == "3") or
        (user_choice == "2" and computer_choice == "1") or
        (user_choice == "3" and computer_choice == "2")
    ):
        return f"{user_name} Menang!"
    else:
        return "Komputer Menang!"

def main():
    print_header()
    user_name = get_user_choice()

    while True:
        print("Pilihlah salah satu pilihan:")
        print("1. batu")
        print("2. kertas")
        print("3. gunting")
        print("Ketik 'exit' untuk keluar")
        user_choice = input("masukkan nomor pilihan Anda (1/2/3): ").lower()

        if user_choice == 'exit':
            break

        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice, user_name)

        print(f"{user_name} memilih {user_choice}")
        print(f"Komputer memilih {computer_choice}")
        print(f"Hasil: {result}")

if __name__ == "__main__":
    main()
