def is_empty_or_spaces(name):
    if name.strip() == "":
        return True
    else:
        return False


class NameInverter:
    honorific = {"Pan", "Pani", "Państwo", "Mr", "Mrs" "Ms"}

    def invert(self, name):
        if name is None:
            raise ValueError
        elif is_empty_or_spaces(name):
            return ""
        else:
            name = name.strip()
            inverted = name.split()
            inverted.reverse()
            inverted_name = ""
            for el in inverted:
                if el in self.honorific:
                    continue
                inverted_name += el + ", "
            return inverted_name[0:-2]
