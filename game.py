def valid_int(question, mini, maxi):  # Function valid
    x = int(input(question))
    while x < mini or x > maxi:
        x = int(input(question))
    return x


def create_file(name_file):  # Function create file
    try:
        f = open(name_file, "wt+")  # (w)write, (t)txt, (+)create file
        f.close()
    except:
        print("Error creating file...")
    else:
        print("File {} created successfully.".format(file))


def file_exists(name_file):  # Function checks for file
    try:
        f = open(name_file, "rt")
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


def list_files(name_file):  # Function list files
    try:
        f = open(name_file, "rt")
    except:
        print("Error reading file.")
    else:
        print(f.read())
    finally:
        f.close()


def register_game(name_file, name_game, name_console):  # Function register game
    try:
        f = open(name_file, "at")
    except:
        print("Error opening file.")
    else:
        f.write("{} - {}\n".format(name_game, name_console))
    finally:
        f.close()


# Main program
file = "Games2.txt"
if file_exists(file):
    print("File {} located on computer.".format(file))
else:
    print("Non existent file.")
    create_file(file)
while True:
    print("MENU:")
    print("1. Register new item")
    print("2. List entries")
    print("3. Exit")
    operator = valid_int("Choose the desired option: ", 1, 3)
    if operator == 1:
        print("Option to register new item selected...\n")
        name_game = input("Game name: ")
        name_console = input("Console name: ")
        register_game(file, name_game, name_console)
    elif operator == 2:
        print("Option to list entries selected...\n")
        list_files(file)
    elif operator == 3:
        print("Ending the program...")
        break
print()
