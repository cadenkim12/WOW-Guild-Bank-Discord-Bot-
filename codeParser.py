class CodeParse:
    def casefold(text):
        return text.lower().strip()

    def ignorespace(text):
        return " ".join(text.strip().split())

    def normalize(text):
        return CodeParse.ignorespace(text).lower()