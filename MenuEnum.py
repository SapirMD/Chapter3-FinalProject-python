from enum import Enum, auto

class MenuOptions(Enum):
    SAVE_NEW_ENTRY = "Save a new entry! (:"
    SEARCH_BY_ID = "Search by ID!"
    PRINT_AGE_AVERAGE = "Print ages average! (:"
    PRINT_ALL_NAMES = "Print all names!"
    PRINT_ALL_IDS = "Print all IDs! (:"
    PRINT_ALL_ENTRIES = "Print all entries!"
    PRINT_ENTRY_BY_INDEX = "Print entry by index! (:"
    SAVE_ALL_DATA = "Save all data!"
    EXIT = "Exit! (:"

class ExitOptions(Enum):
    YES = "y"
    NO = "n"

class EnumHandler():
    def __init__(self, enum_class):
        self._enum_class = enum_class
        self._enum_dict = {}
        self._enum_value_list = []
    
    def getEnumDict(self):
        if not self._enum_dict:
            for index, enum_item in enumerate(self._enum_class):
                self._enum_dict[index + 1] = enum_item
        return self._enum_dict
    
    def getEnumValueList(self):
        if not self._enum_value_list:
            for enum_item in self._enum_class:
                self._enum_value_list.append(enum_item.value)
        return self._enum_value_list
