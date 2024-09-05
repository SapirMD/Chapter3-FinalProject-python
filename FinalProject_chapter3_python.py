import pandas as pd
import json
import os
from Person import Person
from Student import Student
from Employee import Employee
from MenuEnum import MenuOptions, ExitOptions, EnumHandler
import utilities as utils

def printMenu(dict_of_menu_options: dict) -> None:
    for menu_number, enum_member in dict_of_menu_options.items():
        print(str(menu_number) + ". " + enum_member.value)


def saveAllData(db, running_path: str) -> None:
    conf_path = os.path.join(running_path, "conf.json")
    if os.path.exists(conf_path):
        with open(conf_path) as conf_file:
            conf = json.load(conf_file)
    else:
        print("Error: Config file conf.json is missing in path " + os.getcwd())
        return
    data = {}
    for key, person in db.items():
        data[key] = {"type": person.getType()}
        data[key].update(person.getAttributesDict())
    df = pd.DataFrame(data).T # Transpose - changing the orientation of rows to columns
    output_f_path = createOutputFilePath(running_path)
    if output_f_path == None:
        return
    df.reset_index(inplace=True) # Includes id as a column
    df.rename(columns={"index": conf["id"]}, inplace=True)
    for field in conf:
        df.rename(columns={field: conf[field]}, inplace=True)    
    df.to_csv(output_f_path, index=False)
    print("Data was saved successfully.")


def createOutputFilePath(running_path: str) -> str:
    output_f_name =  input("What is your file output name? ")
    if not ".csv" in output_f_name:
        if "." in output_f_name:
            print("Error: Please enter a name without any file extension OR Enter a valid csv file extension(.csv)")
            return None
        output_f_path = os.path.join(running_path, output_f_name + ".csv")
    if os.path.exists(output_f_path):
        print("Warning: A file with the name " + output_f_name +  ".csv already exists.")
        user_choice = ""
        while user_choice != "y" and user_choice != "n":
            user_choice = input("Do you want to override it? (y/n) ")
            if user_choice == "n":
                print("Data was not saved.")
                return None
            elif user_choice == "y":
                break
    return output_f_path


# Change first_gap of "ID" base on need
def printEntry(db: dict, id_wanted: int, first_gap: str = "   ") -> None: 
    class_name = "(" + db[id_wanted].getType() + ")"
    print(first_gap + class_name)
    print("   ID: " + str(id_wanted))
    print(db[id_wanted])


# Saving a valid entry to db & Returns 0 on error
def saveNewEntry(db: dict) -> int:
    id_input = input("ID: ") 
    if not isNewIdValid(db, id_input):
        return 0
    types = [Student, Employee, Person]
    print("Is the person:")
    for index, type in enumerate(types):
        print("     " + str(index) + ". " +  type.__name__)
    try:
        user_choice = utils.handleUserChoice("Your choice", len(types))
    except ValueError:
        return 0
    new_person = types[int(user_choice)]()
    db[id_input] = new_person
    
    print("ID [" + id_input + "] saved successfully")
    return new_person.getAge()


def isNewIdValid(db: dict, id: int) -> bool:
    if not utils.isNumber(id, "ID"):
        return False
    if id in db:
        print("Error: ID already exists: ")
        printEntry(db, id)
        return False
    return True


def searchById(db: dict) -> None:
    id_wanted = input("Please enter the ID you want to look for: ")
    if not utils.isNumber(id_wanted, "ID"):
        return
    if not id_wanted in db:
        print("Error: ID " + id_wanted + " is not saved")
        return
    printEntry(db, id_wanted)


def printAgesAverage(db: dict, age_sum) -> None:
    if len(db) == 0:
        print(0)
        return
    average = age_sum / len(db)
    print(average)


def printAllNames(db: dict) -> None:
    for index, key in enumerate(db):
        print(str(index) + ". " + db[key].getName())


def printAllIds(db: dict) -> None:
    for index, key in enumerate(db):
        print(str(index) + ". " + key)


def printAllEntries(db: dict) -> None:
    for index, key in enumerate(db):
        first_gap = str(index) + ". "
        printEntry(db, key, first_gap)


def printEntryByIndex(db: dict) -> None:
    db_last_index = len(db) - 1
    wanted_index = input("Please enter the index of the entry you want to print: ")
    if not utils.isNumber(wanted_index, "index"):
        return 
    wanted_index = int(wanted_index)
    if wanted_index > db_last_index :
        print("Error: Index out of range. The maximum index allowed is " + str(db_last_index))
        return
    for index, key in enumerate(db):
        if wanted_index == index:
            printEntry(db, key)
            return


def router() -> None:
    # db --> { "id": { Person } }
    db = {}
    age_sum = 0
    running_path = "C:\\Users\\sapir\\Desktop\\py\\FinalProject_chapter3_python"
    dict_of_menu_options = EnumHandler(MenuOptions).getEnumDict()
    list_of_exit_options = EnumHandler(ExitOptions).getEnumValueList()

    while True:
        printMenu(dict_of_menu_options)
        try:
            user_choice = utils.handleUserChoice("Your choice", len(dict_of_menu_options))
        except ValueError:
            continue
        user_choice = dict_of_menu_options[user_choice]
        match user_choice:
            case MenuOptions.SAVE_NEW_ENTRY:
                age_sum += saveNewEntry(db)
            case MenuOptions.SEARCH_BY_ID:
                searchById(db)
            case MenuOptions.PRINT_AGE_AVERAGE:
                printAgesAverage(db, age_sum)
            case MenuOptions.PRINT_ALL_NAMES:
                printAllNames(db)
            case MenuOptions.PRINT_ALL_IDS:
                printAllIds(db)
            case MenuOptions.PRINT_ALL_ENTRIES:
                printAllEntries(db)
            case MenuOptions.PRINT_ENTRY_BY_INDEX:
                printEntryByIndex(db)
            case MenuOptions.SAVE_ALL_DATA:
                saveAllData(db, running_path)
            case MenuOptions.EXIT:
                while user_choice not in list_of_exit_options:
                    user_choice = input("Are you sure? (" + "/".join(list_of_exit_options) + ") ")
                if user_choice == ExitOptions.YES.value:
                    print("Goodbye!")
                    break
            case _:
                utils.errorMessage(user_choice)
        input("Press Enter to continue")


if __name__ == "__main__":
    router()
        