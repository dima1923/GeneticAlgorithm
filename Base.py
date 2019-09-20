class Base:
    def __init__(self, type, **kwargs):
        if hasattr(self.__class__, type):
            self.method = getattr(self.__class__, type)(kwargs)
        else:
            raise NotImplemented