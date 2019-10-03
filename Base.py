class Base:
    def __init__(self, types, **kwargs):
        if hasattr(self.__class__, types):
            self.types = types
            self.kwargs = kwargs
        else:
            raise NotImplemented

    def __call__(self, **kwargs):
        return getattr(self.__class__, self.types)(self, **kwargs)