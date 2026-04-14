from RawMats import RawMats

class cmds:
    def get(cmd):
        if cmd.startswith("/get"):
            item = cmd.strip()[5:].strip()
            stock = RawMats.getstock(item)
            target = RawMats.gettarget(item)
            notes = RawMats.getnotes(item)

            if stock is None:
                return "Item not found."

            return f"In Stock: {stock}, Target Amount: {target}, Notes: {notes}"
        return "Something went wrong while fetching that item."

    def help(cmd):
        if cmd.startswith("/help"):
            return (
                "/get [item]: Gives the amount in Guild Bank and Target Amount\n"
                "/refresh: Reloads the Google Sheet data"
            )
        return None