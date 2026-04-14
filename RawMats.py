import gspread
from codeParser import CodeParse

gc = gspread.service_account(filename="service_account.json")
sh = gc.open("Wow Karazhan Chess Team GB v.2_5.31.2025")
worksheet = sh.get_worksheet(2)


class RawMats:
    def refresh():
        RawMats.worksheetvals = worksheet.get_all_values()
        RawMats.current_inventory = worksheet.col_values(1)
        RawMats.current_stock = worksheet.col_values(2)
        RawMats.current_target = worksheet.col_values(3)
        RawMats.current_notes = worksheet.col_values(4)

    def find_index(word_index):
        if word_index is None:
            return None
        for i in range(len(RawMats.current_inventory)):
            if RawMats.current_inventory[i].startswith(word_index):
                return i
        return None

    def getListof(startindex, endindex):
        start = RawMats.find_index(startindex)
        if start is None:
            return []

        if endindex is None:
            end = len(RawMats.current_inventory)
        else:
            end = RawMats.find_index(endindex)
            if end is None:
                end = len(RawMats.current_inventory)

        invlist = RawMats.current_inventory[start + 1:end]
        return [item for item in invlist if item.strip() != ""]

    def getInventory():
        return worksheet.get_all_values()

    def itemlist():
        start = RawMats.find_index("Mining")
        if start is None:
            return []
        return [item for item in RawMats.current_inventory[start:] if item.strip() != ""]

    def _find_item_row(itemToGrab):
        wanted = CodeParse.normalize(itemToGrab)
        for i in range(len(RawMats.current_inventory)):
            current = CodeParse.normalize(RawMats.current_inventory[i])
            if current == wanted:
                return i
        return None

    def getitem(itemToGrab):
        i = RawMats._find_item_row(itemToGrab)
        if i is not None:
            return RawMats.current_inventory[i]
        return None

    def getstock(itemToGrab):
        i = RawMats._find_item_row(itemToGrab)
        if i is not None:
            return RawMats.current_stock[i]
        return None

    def gettarget(itemToGrab):
        i = RawMats._find_item_row(itemToGrab)
        if i is not None:
            return RawMats.current_target[i]
        return None

    def getnotes(itemToGrab):
        i = RawMats._find_item_row(itemToGrab)
        if i is not None:
            return RawMats.current_notes[i]
        return None

    def switchlist(control):
        if control == 0:
            return RawMats.getListof("Mining", "Leatherworking")
        if control == 1:
            return RawMats.getListof("Leatherworking", "Cloth")
        if control == 2:
            return RawMats.getListof("Cloth", "Enchanting")
        if control == 3:
            return RawMats.getListof("Enchanting", "Alchemy/ Herbalism")
        if control == 4:
            return RawMats.getListof("Alchemy/ Herbalism", "Fishing/Cooking")
        if control == 5:
            return RawMats.getListof("Fishing/Cooking", None)
        return []


RawMats.refresh()