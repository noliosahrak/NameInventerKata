class NameInverter:

    def invert(self, name):
        if name is None:
            raise ValueError
        else:
            return name.strip()
