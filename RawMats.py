import gspread 
gc = gspread.service_account()
sh = gc.open("Wow Karazhan Chess Team GB v.2_5.31.2025")

worksheet = sh.get_worksheet(2)
worksheetvals = worksheet.get_all_values()

current_inventory = worksheet.col_values(1)
current_stock = worksheet.col_values(2)
current_target = worksheet.col_values(3)
current_notes = worksheet.col_values(4)

class RawMats:
    # subclass for profession 
    # creates a list of items from a profession 
        
        def find_index(WordIndex):
            for i in range(len(worksheetvals)):
                if current_inventory[i].startswith(WordIndex):
                    return i 
        
        def getListof(startindex, endindex):
            start = RawMats.Profession.find_index(startindex)
            end = RawMats.Profession.find_index(endindex)

            invlist = current_inventory[start+1:end]
            filteredlist = [item for item in invlist if item != '']
            return filteredlist
        
        def itemlist():
            for i in range(len(worksheetvals)):
                if current_inventory[i].startswith("Mining"):
                    end = i 
                    continue
            return current_inventory[end:]

        def getitem(itemTograb):
            for i in range(len(worksheetvals)):
                if current_inventory[i].startswith(itemTograb):
                    return current_inventory[i]
                
        def getstock(itemTograb):
            for i in range(len(worksheetvals)):
                if current_inventory[i].startswith(itemTograb):
                    return current_stock[i]
                
        def gettarget(itemTograb):
            for i in range(len(worksheetvals)):
                if current_inventory[i].startswith(itemTograb):
                    return current_target[i]
                
        def getnotes(itemTograb):
            for i in range(len(worksheetvals)):
                if current_inventory[i].startswith(itemTograb):
                    return current_notes[i]
        
        def switchlist(control):
            if control == 0:
                result =  RawMats.getListof("Mining", "Leatherworking")
            if control == 1:
                result = RawMats.getListof("Leatherworking", "Cloth")
            if control == 2:
                result = RawMats.getListof("Cloth", "Enchanting")
            if control == 3:
                result = RawMats.getListof("Enchanting", "Alchemy/ Herbalism")    
            if control == 4:
                result = RawMats.getListof("Alchemy/ Herbalism", "Fishing/Cooking")
            if control == 5:
                result = RawMats.getListof("Blacksmith", None)
            return result
            
            
