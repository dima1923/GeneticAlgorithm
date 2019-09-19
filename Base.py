class Base:
    def __init__(self, type):
        if hasattr(self.__class__,type):
            self.type = getattr(self.__class__, type)
        else:
            raise NotImplementedError